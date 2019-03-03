#!/usr/bin/env python3

from sys import argv
from json import dump
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import subprocess

from write import to_markdown


def scrape_page(address: str):
    result = {}
    html = requests.get(address)
    root = BeautifulSoup(html.text, 'html.parser')

    result["name"] = root.select(".firstHeading")[0].get_text().replace(" ", "_")

    ## Notes/Warnings/Versions/Tips
    # All the messages displayed about usage
    # errors, information, deprecation and versioning
    notes = None
    warnings = None
    versions = None
    tips = None
    outdated = None
    lowercase = None
    table = root.select("table a.image")
    if table:
        for element in table:
            parent = element.find_parent("td")
            if parent:
                td = parent.find_next_sibling("td")
                if td is not None:
                    span = td.select("span")[0]
                    if element.has_attr("href"):
                        href = element["href"]
                        # Version
                        if href == "/wiki/Image:Add.png":
                            versions = span.get_text()
                        # Warnings
                        elif href == "/wiki/Image:32px-Circle-style-warning.png":
                            warnings = span.get_text()
                        # Notes
                        elif href == "/wiki/Image:32px-Ambox_warning_orange.png":
                            notes = span.get_text()
                        # Tips
                        elif href == "/wiki/Image:Light_bulb_icon.png":
                            tips = span.get_text()
                        # Outdated
                        elif href == "/wiki/Image:50px-Ambox_outdated_serious.png":
                            outdated = span.get_text()
                        # Lowercase
                        elif href == "/wiki/Image:Farm-Fresh_text_lowercase.png":
                            result["name"] = result["name"].lower()

    result["notes"] = notes
    result["warnings"] = warnings
    result["versions"] = versions
    result["tips"] = tips
    result["outdated"] = outdated
    result["lowercase"] = lowercase

    ## Description
    # The pages descripton
    description = root.select(".description")
    if description:
        result["description"] = description[0].get_text()

    ## Params
    # The parameters a callback / native accepts
    params_title = root.select(".parameters")
    if params_title:
        result["params_title"] = params_title[0].get_text()
    params_body = []
    for param in root.select(".param"):
        columns = param.select("td")
        params_body.append({
            "name": columns[0].get_text(),
            "description": columns[1].get_text()
        })
    result["params_body"] = params_body

    ## Return Values
    # The value returned from a native or callback
    return_values = None
    b = root.select(".param")
    if b:
        p = b[0].find_next_sibling("p")
        if p:
            div = p.find_next_sibling("div")
            if div:
                ul = div.select("ul")
                if ul:
                    lines = []
                    for li in ul[0].select("li"):
                        lines.append(li.get_text())
                    return_values = '\n'.join(lines)
                else:
                    return_values = div.get_text()
    result["return_values"] = return_values

    ## Code Blocks
    # Contains code or config variables for code blocks
    pawn = []
    code = []
    pre = root.select("pre")
    if pre:
        for element in pre:
            if element.has_attr("class") and element["class"][0] == "pawn":
                pawn.append(element.get_text())
            else:
                code.append(element.get_text())
    result["pawn_code"] = pawn
    result["code"] = code

    ## Related Functions
    # Links to related natives
    related_fn = []
    element = root.select("a[name=\"Related_Functions\"]")
    if element:
        next_element = element[0].find_next_siblings("ul")
        if next_element:
            for ul in next_element:
                for li in ul.select("li"):
                    related_fn.append(li.get_text())
    result["related_fn"] = related_fn

    ## Related Callbacks
    # Links to related callbacks
    related_cb = []
    element = root.select("a[name=\"Related_Callbacks\"]")
    if element:
        next_element = element[0].find_next_siblings("ul")
        if next_element:
            for ul in next_element:
                for li in ul.select("li"):
                    related_cb.append(li.get_text())
    result["related_cb"] = related_cb

    return result


def get_functions_from(address: str):
    # perform a HTTP GET request on the scripting functions page
    # `functions` now contains a response object
    functions = requests.get(address)
    # get the text out of the response body (the raw HTML code) and parse it using
    # beautifulsoup, this gives us a root node
    root = BeautifulSoup(functions.text, 'html.parser')

    # do a CSS select to get all the elements we want
    content = root.select("#bodyContent > table:nth-child(101) a")

    # iterate through the results and print the href attribute
    pages = []
    for node in content:
        address = "https://wiki.sa-mp.com" + node['href']
        pages.append(address)

    return pages


def main():
    start_from = None
    if len(argv) > 1:
        start_from = argv[1]

    all_pages = []
    pages = []

    all_pages += get_functions_from(
        "https://wiki.sa-mp.com/wiki/Category:Scripting_Functions")
    all_pages += get_functions_from(
        "https://wiki.sa-mp.com/wroot/index.php?title=Category:Scripting_Functions&from=GetPlayerPing")
    all_pages += get_functions_from(
        "https://wiki.sa-mp.com/wroot/index.php?title=Category:Scripting_Functions&from=SetPlayerCameraPos")

    if start_from is not None:
        get = False
        for p in all_pages:
            if get:
                pages.append(p)
            else:
                if p.rsplit("/", 1)[1] == start_from:
                    get = True
    else:
        pages = all_pages

    print("Pages to scrape:", len(pages))

    for page in pages:
        print(f"Pricessing {page}")

        try:
            page_data = scrape_page(page)
            page_markdown = to_markdown(page_data)
        except Exception as e:
            print(e)
            continue

        name = page_data["name"]
        path_json = f"functions/{name}.json"
        path_markdown = f"markdown/{name}.md"

        page_markdown_formatted = subprocess.run(
            ["prettier", "--parser=markdown"],
            encoding='utf8',
            input=page_markdown,
            stdout=subprocess.PIPE,
        ).stdout

        with open(path_json, 'w') as fp:
            dump(page_data, fp)

        with open(path_markdown, 'w') as fp:
            fp.write(page_markdown_formatted)

main()
