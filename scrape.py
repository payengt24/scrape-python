import pandas as pd
import requests 
from bs4 import BeautifulSoup

page =  requests.get('https://forecast.weather.gov/MapClick.php?lat=45.04790500000007&lon=-93.34837999999996')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = (week.find_all(class_ = "tombstone-container"))

# print(items[0])

# for i in items:
#     print(i.find(class_ ='period-name').get_text())
#     print(i.find(class_ ='short-desc').get_text())
#     print(i.find(class_ ='temp').get_text())

period_name = [item.find(class_ = 'period-name').get_text() for item in items]    
short_desc = [item.find(class_ = 'short-desc').get_text() for item in items]    
temp = [item.find(class_ = 'temp').get_text() for item in items]    

# print(period_name)
# print(short_desc)
# print(temp)

weather_stuff = pd.DataFrame(
    {'period': period_name,
    'short_desc': short_desc ,
    'temp': temp }
)

print(weather_stuff)

weather_stuff.to_csv('weather.csv')

