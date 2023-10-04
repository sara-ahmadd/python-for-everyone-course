# import urllib, urllib.request, urllib.parse
# from bs4 import BeautifulSoup

# file = urllib.request.urlopen(
#     "https://py4e-data.dr-chuck.net/comments_1897758.html"
# ).read()


# def main(page):
#     parsed_data = BeautifulSoup(page, "lxml")
#     table = parsed_data.find("table")
#     body = table.find_all("span", {"class": "comments"})
#     summation = 0
#     for i in range(len(body)):
#         summation = summation + int(body[i].text.strip())
#     print(summation)


# main(file)


import urllib, urllib.request, urllib.parse
from bs4 import BeautifulSoup


count = input("Enter Count: ")
position = input("Enter Position: ")
url = input("Enter Url : ")

pos = int(position)
count = int(count)

while count > 0:
    print(f"Retrieving: {url}")
    if count == 0:
        break
    file = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(file, "html.parser")
    tags = soup("a")
    name = tags[pos - 1].text.strip()
    url = tags[pos - 1].get("href", None)
    count -= 1
