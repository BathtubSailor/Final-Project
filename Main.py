from ScrapeWebsite import ScrapeWebsite
from DisplayData import DisplayData
from DisplayBetterData import DisplayBetterData
Test = ScrapeWebsite()
print(Test.scrape_country('France',"https://www.worldometers.info/coronavirus"))
DisplayData("ScrapeJson.json")






