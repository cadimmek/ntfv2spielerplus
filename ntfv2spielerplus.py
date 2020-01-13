import sys

from ics import Calendar
import requests
import csv

url = 'https://ntfv.de/liga-nord-west-155/tabellen-a-ligaspiele?task=team_begegnungen_ical&id=952'
data = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text

c = Calendar(data)

for e in c.timeline:
    start = e.begin.to('Europe/Berlin').format('DD.MM.YYYY')
    end = e.end.to('Europe/Berlin').format('DD.MM.YYYY')
    time = e.end.format('HH:mm:ss')
    print(start, end, time)





