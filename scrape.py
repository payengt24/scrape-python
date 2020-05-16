import requests 
from bs4 import BeautifulSoup

page =  requests.get('https://forecast.weather.gov/MapClick.php?lat=45.04790500000007&lon=-93.34837999999996')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('a'))