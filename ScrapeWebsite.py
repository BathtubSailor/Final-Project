# Project Instructions copied from Canvas

#  "we will stick to visualizing death rates"
#  In this phase, you will focus on collecting data from the web in order to compute the following metrics:
#  -Daily death rates
#  -Cumulative death rates


from bs4 import BeautifulSoup
import requests
import json

class ScrapeWebsite():
    def scrape_country(self, countryName, website):
        
        if website != "https://www.worldometers.info/coronavirus":
            print('ERROR - website not supported :', website)
            return -1

        page = requests.get(website)
        soup = BeautifulSoup(page.text, "lxml")

        table = soup.find("table", id = "main_table_countries_today")

        body = table.find_all("tbody")[0]
        rows = body.find_all('tr',style = '')
        output = []

        for i in range(1,100):
            row = rows[i].get_text().split('\n')
            #print(":",row[2],":",row[5].strip(),":",row[6])
            temp = {}

            temp["Country"] = str(row[2])
            try:
                temp["Total Deaths"] = int(row[5].replace(',',''))
            except:
                temp["Total Deaths"] = 0
            try:
                temp["New Deaths"] = int(row[6].split('+')[1])
            except:
                temp["New Deaths"] = 0
            try:
                temp["Normalized Deaths"] = int(row[12].replace(',',''))
            except:
                temp["Normalized Deaths"] = 0

            output.append(temp)

        with open("ScrapeJson.json","w") as outfile:
            json.dump(output, outfile)


        itemFound = 0
        for i in output:
            if i['Country'] == countryName:
                return i
                itemFound = 1
                break
        if not itemFound:
            print('Error - Country not found!')
            return -1






#    jsonObj = [{
#    "country": "India",
#    "totalCases": 200,
#    "toatlDeaths": 50
#},{
#    "USA": 100
#}]
#(2) [{…}, {…}]
#jsonObj.length
#2
#jsonObj[0].country
#'India'
#jsonObj[0].toatlDeaths
#50
#jsonObj[0].totalCases
#200
#jsonObj[1]
#{USA: 100}USA: 100[[Prototype]]: Object




