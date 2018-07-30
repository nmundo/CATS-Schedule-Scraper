## Script to scrape train schedule from CATS' website

from bs4 import BeautifulSoup

import requests

inboundTimetable = {}

r = requests.get('http://wirelesscats.ridetransit.org/BusSchedules/Search/PrinterVersion?bookingId=78&routeId=6545&routeType=Weekday&busRouteId=6545')

soup = BeautifulSoup(r.content, 'html.parser')

inboundSchedule = soup.find(id='inboundTable')

i = 0
for i in range(0, 26):
    inboundTimetable[i] = []

print(inboundTimetable)

for row in inboundSchedule.find('tbody').find_all('tr'):
    print('New row')
    i = 0
    for column in row.find_all('td'):
        print(i)
        print(column.get_text().strip())
        inboundTimetable[i].append(column.get_text().strip())
        i += 1

print(inboundTimetable)



