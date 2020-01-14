import ics
import requests
import csv
import constant

team_name = 'Devilution'
url = 'https://ntfv.de/liga-nord-west-155/tabellen-a-ligaspiele?task=team_begegnungen_ical&id=952'
data = requests.get(url, headers={"User-Agent": "Script"}).text
# True => Spiele müssen zugesagt werden, False => Spiele müssen abgesagt werden
active = True

export_headers = [
    'Spieltyp',
    'Gegner',
    'Datum',
    'End-Datum',
    'Treffen (Optional)',
    'Startzeit',
    'Ende (Optional)',
    'Heimspiel',
    'Gelände / Räumlichkeiten',
    'Infos zum Spiel',
    'Teilname',
    'Zu-/Absagen bis (x Stunden vor dem Termin)',
    'Erinnerung zum Zu-/Absagen(x Stunden vor dem Termin)'
]

c = ics.Calendar(data)

with open('./calender.csv', mode='w') as calender:
    csv_writer = csv.writer(calender, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(export_headers)

    for e in c.timeline:
        start = e.begin.to(constant.TZ)
        end = e.end.to(constant.TZ)
        home = e.name.startswith(team_name)
        csv_writer.writerow([
            'Spiel',
            e.name,
            start.format(constant.DATE_FORMAT),
            end.format(constant.DATE_FORMAT),
            start.shift(hours=-1).format(constant.TIME_FORMAT),
            start.format(constant.TIME_FORMAT),
            end.format(constant.TIME_FORMAT),
            'ja' if home else 'nein',
            e.location,
            e.description,
            'Spieler müssen zusagen' if active else 'Spieler müssen absagen',
            24,
            72
        ])
