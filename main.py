## Script to scrape train schedule from CATS' website

from bs4 import BeautifulSoup
import requests
import json

inboundTimetable = {}
outboundTimetable = {}

r = requests.get('http://wirelesscats.ridetransit.org/BusSchedules/Search/PrinterVersion?bookingId=78&routeId=6545&routeType=Weekday&busRouteId=6545')

soup = BeautifulSoup(r.content, 'html.parser')

inboundSchedule = soup.find(id='inboundTable')
outboundSchedule = soup.find(id='outboundTable')

i = 0
for i in range(0, 26):
    inboundTimetable[i] = []
    outboundTimetable[i] = []

for row in inboundSchedule.find('tbody').find_all('tr'):
    print('New row')
    i = 25
    for column in row.find_all('td'):
        print(i)
        print(column.get_text().strip())
        inboundTimetable[i].append(column.get_text().strip())
        i -= 1

for row in outboundSchedule.find('tbody').find_all('tr'):
    print('New row')
    i = 0
    for column in row.find_all('td'):
        print(i)
        print(column.get_text().strip())
        outboundTimetable[i].append(column.get_text().strip())
        i += 1


print(inboundTimetable)
print(outboundTimetable)

with open('inbound.json', 'w') as fp:
    json.dump(inboundTimetable, fp)

with open('outbound.json', 'w') as fp:
    json.dump(outboundTimetable, fp)
