# Covid Data Scraper

(README) - Anthony Eiting & Daniel Sturm
This project will require the following python libraries
to be pip installed your computer:

BeautifulSoup4
Requests
json
Bokeh

With these libraries installed you will need to download the following 3 scripts:
Main, ScrapeWebsite, DisplayData.  At the time of this publication DisplayData
is incomplete and only displayes a single set of data.  The program should be
executed from the Main.py script with the ScrapeWebsite.py & DisplayData.py
located in the same file directory.
______________
Functionality:

The Main.py is meant for executing the other two scripts.  For the function
requirement of this project - the website is already input into the class
object function - the user can edit the country field to have the stats of a
given country returned on the cmd.

The ScrapeWebsite.py scripte utilizes the BeautifulSoup libraries to pull data
from Worldometer.com.  This is accomplished by pulling in the HTML code as a 
searchable text file.  From there, the strings are pulled out of the table
row headings <td> using .get_text() and sorted/separated by ','.  These are then
restructured into dictionaries that are output into a .json file which has been
uploaded here on the project.

The DisplayData.py is incomplete at this time, but currently utilizes the
Bokeh library to create a useful graphic for the user to compair death rates
 due to covid by country.



