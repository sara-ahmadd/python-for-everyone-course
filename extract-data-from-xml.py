import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


loc = input("Enter Location : ")

page = urllib.request.urlopen(loc).read()


def main(p):
    summation = 0
    if len(p) > 0:
        tree = ET.fromstring(page)
        lst = tree.findall("comments/comment/count")
        for i in lst:
            summation += int(i.text)
    return summation


print(main(page))
