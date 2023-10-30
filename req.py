import requests
import json

start=3050

with open('C:/Users/apskaita3/Desktop/number.txt') as f:
    start= f.readlines()
    
start=int(start[0])

start=start+40
results = {"item": {}}
# Todo load json
for i in range(0,9801): #<----- Just change range here to increase number of requests
    URL = f"https://api.news.eu.nasdaq.com/news/query.action?displayLanguage=en&timeZone=Europe%2FTallinn&dateMask=yyyy-MM-dd+HH%3Amm%3Ass+Z&limit=100&countResults=false&start={i}&fromDate=1285891200000&toDate=1577750400000&company=Telia+Lietuva%2C+AB&releaseMarket=Main+Market%2C+Tallinn&releaseMarket=Main+Market%2C+Riga&releaseMarket=Main+Market%2C+Vilnius&releaseMarket=First+North+Estonia&releaseMarket=First+North+Latvia&releaseMarket=First+North+Lithuania&callback=jQuery22408949616114501848_1698132799166&_=1698132799179"
    r = requests.get(url = URL)
    print(r)
    print("Doing: " + str(i + 1) + "th")
    data = r.json()
    downloaded_entries = data["results"]["item"]
    new_entries = [d for d in downloaded_entries if d["headline"] not in results["item"]]
    start=str(start)
    for entry in new_entries:
         headline = entry["headline"]
         published = entry["published"]
         published=published>="2022-05-01"
         results["item"][headline] = {"company": entry["company"], "messageUrl": entry["messageUrl"], "published": entry["published"], "headline": headline}
print(results)
with open("C:/Users/apskaita3/Finansų analizės ir valdymo sprendimai, UAB/Rokas Toomsalu - Power BI analitika/Integracijos/1_Public comapnies analytics/Databasesets/Others/market_news.json", "w") as outfile:    
    json_object = json.dumps({"item": list(results["item"].values())}, indent = 4)
    print(json_object)
    outfile.write(json_object)
with open("C:/Users/apskaita3/Desktop/number.txt", "w") as outfile1:    
    outfile1.write(start)