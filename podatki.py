import requests
from bs4 import BeautifulSoup
import csv

vse_olimpijske = {}
pz_olimpijske = {}

url = 'https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table#Complete_ranked_medals_(excluding_precursors)'
response = requests.get(url)

polet_igre = response.text.split('<span class="mw-headline" id="Complete_ranked_medals_(excluding_precursors)">Complete ranked medals (excluding precursors)</span>')[1]

soup = BeautifulSoup(polet_igre, 'html.parser')

table = soup.find('table', {'class': 'multicol'})

table_2 = table.find('table',{'class' : 'wikitable sortable plainrowheaders jquery-tablesorter'})

rows = table_2.find('tbody').find_all('tr')[1:-1]

with open('poletne_olimpijske.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Država', 'Zlata', 'Srebrna', 'Bronasta', 'Skupaj'])
      
    for row in rows:
        Država = row.find('a').text.strip()
        tab = row.find_all('td')
        Zlata = int(tab[-4].text.strip())
        Srebrna = int(tab[-3].text.strip())
        Bronasta = int(tab[-2].text.strip())
        Skupaj = int(tab[-1].text.strip())
        writer.writerow([Država, Zlata, Srebrna, Bronasta, Skupaj])
        vse_olimpijske[Država] = [Zlata, Srebrna, Bronasta, Skupaj]
        pz_olimpijske[Država] = [Zlata, Srebrna, Bronasta, Skupaj, 0, 0, 0, 0]


zimske_igre = response.text.split('<span class="mw-headline" id="Winter_Olympics_(1924–2022)">Winter Olympics (1924–2022)</span>')[1]

soup = BeautifulSoup(zimske_igre, 'html.parser')

rows = soup.find('tbody').find_all('tr')[1:-1]
  
with open('zimske_olimpijske.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Država', 'Zlata', 'Srebrna', 'Bronasta', 'Skupaj'])
      
    for row in rows:
        Država = row.find('a').text.strip()
        tab = row.find_all('td')
        Zlata = tab[-4].text.strip()
        Srebrna = tab[-3].text.strip()
        Bronasta = tab[-2].text.strip()
        Skupaj = tab[-1].text.strip()
        writer.writerow([Država, Zlata, Srebrna, Bronasta, Skupaj])
        if Država in vse_olimpijske:
            zl, sr, br, sk = vse_olimpijske[Država]
            vse_olimpijske[Država] = [int(zl) + int(Zlata), int(sr) + int(Srebrna), int(br) + int(Bronasta), int(sk) + int(Skupaj)]
        else:
            vse_olimpijske[Država] = [Zlata, Srebrna, Bronasta, Skupaj]
        if Država in pz_olimpijske:
            pz_olimpijske[Država] = pz_olimpijske[Država][:4] + [Zlata, Srebrna, Bronasta, Skupaj]
        else:
            pz_olimpijske[Država] = pz_olimpijske.get(Država, [0,0,0,0]) + [Zlata, Srebrna, Bronasta, Skupaj]


with open('vse_olimpijske.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Država', 'Zlata', 'Srebrna', 'Bronasta', 'Skupaj'])
    for drzava in vse_olimpijske:
        Zlata, Srebrna, Bronasta, Skupaj = vse_olimpijske[drzava][0], vse_olimpijske[drzava][1], vse_olimpijske[drzava][2], vse_olimpijske[drzava][3]
        writer.writerow([drzava, Zlata, Srebrna, Bronasta, Skupaj])
        
with open('pz_olimpijske.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Država', 'Zlata', 'Srebrna', 'Bronasta', 'Skupaj'])
    for drzava in pz_olimpijske:
        pzl, psr, pbr, psk, zzl, zsr, zbr, zsk = pz_olimpijske[drzava][0], pz_olimpijske[drzava][1], pz_olimpijske[drzava][2], pz_olimpijske[drzava][3], pz_olimpijske[drzava][4], pz_olimpijske[drzava][5], pz_olimpijske[drzava][6], pz_olimpijske[drzava][7]
        writer.writerow([drzava, pzl, psr, pbr, psk, zzl, zsr, zbr, zsk])

    
