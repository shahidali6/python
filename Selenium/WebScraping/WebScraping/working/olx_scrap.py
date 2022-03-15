URL = baseURL + "/product-category/frozen"
page = requests.get(URL, cookies_dict)
curSession = requests.Session()
getCookies = curSession.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="ResultsContainer")
results = soup.find(class_="ba608fb8")
print(results)

allElements = results.find_all("article", class_="_7e3920c1")

print("=========================================================")

status = "No element found"

myList = []

for element in allElements:
    innerList = []
    try:
        title = element.find("div", class_="a5112ca8").text.strip()
        print(title)
        innerList.append(title)
    except:
        print(status)
        innerList.append(status)

    try:
        priceStart = element.find("div", class_="_52497c97").span.text.strip().replace(
            "Rs", "").replace(",", "").strip()
        priceEnd = ""
        if '|' in priceStart:
            priceSplit = priceStart.split('|')
            if len(priceSplit) > 0:
                finalSplit = priceSplit[0].split('-')
                priceStart = finalSplit[0]
                priceEnd = finalSplit[1]
        print(priceStart + " | "+priceEnd)
        innerList.append(priceStart)
        innerList.append(priceEnd)
    except:
        print("0|0")
        innerList.append(0)
        innerList.append(0)

    try:
        location = element.find("span", class_="_424bf2a8").text.strip()[:-1]
        print(location)
        innerList.append(location)
    except:
        print(status)
        innerList.append(status)

    try:
        image = element.find("source").get('srcset').strip()
        print(image)
        innerList.append(image)
    except:
        print(status)
        innerList.append(status)

    try:
        link = baseURL + \
            element.find("div", class_="ee2b0479").a.get('href').strip()
        print(link)
        innerList.append(link)
    except:
        print(status)
        innerList.append(status)

    try:
        feature = element.find("span", class_="_151bf64f").text.strip()
        print(feature)
        innerList.append(feature)
    except:
        print(status)
        innerList.append(status)

    print(innerList)
    print("--------Next---------")
    if innerList[6] == status:
        myList.append(innerList)

CSV.WriteCSVFile("olx", myList)
InsertDataIntoMySQL(myList)
print("=========================================================")
