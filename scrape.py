#!/usr/bin/env python3

from json import dumps
from bs4 import BeautifulSoup
import requests


def scrape_page(address: str):
    result = {}
    html = requests.get(address)
    root = BeautifulSoup(html.text, 'html.parser')

    result["description"] = root.select(".description")[0].get_text()
    result["feature"] = root.select("#bodyContent > div > table")[0].get_text()
    params = []
    for param in root.select(".param"):
        columns = param.select("td")
        params.append({
            "name": columns[0].get_text(),
            "description": columns[1].get_text()
        })
    result["params"] = params

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
    pages = []

    pages += get_functions_from(
        "https://wiki.sa-mp.com/wiki/Category:Scripting_Functions")
    pages += get_functions_from(
        "https://wiki.sa-mp.com/wroot/index.php?title=Category:Scripting_Functions&from=GetPlayerPing")
    pages += get_functions_from(
        "https://wiki.sa-mp.com/wroot/index.php?title=Category:Scripting_Functions&from=SetPlayerCameraPos")

    print("Pages to scrape:", len(pages))

    for page in pages:
        scrape_page(page)


# main()
print(dumps(scrape_page("https://wiki.sa-mp.com/wiki/CreatePlayerTextDraw")))
