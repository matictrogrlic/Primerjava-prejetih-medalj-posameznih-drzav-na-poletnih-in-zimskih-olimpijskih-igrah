import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

subprocess.run(['python', 'podatki.py']) # posodobimo podatke, ki jih pridobimo v datoteki: podatki.py

# seznami držav po celinah
evropa = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Holy See', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom']
afrika = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Comoros', 'Republic of the Congo', 'Democratic Republic of the Congo', 'Côte d\'Ivoire', 'Djibouti', 'Equatorial Guinea', 'Egypt', 'Eritrea', 'Ethiopia', 'Gabon', 'The Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Réunion', 'Rwanda', 'São Tomé and Príncipe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Swaziland', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Western Sahara', 'Zambia', 'Zimbabwe']
antarctica = []
azija = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'East Timor', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'The Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'The Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']
severna_amerika = ['Canada', 'Mexico', 'United States of America', 'Navassa Island', 'Puerto Rico', 'US Virgin Islands', 'Dominican Republic', 'Cuba', 'Greenland', 'Haiti', 'Belize', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Guadeloupe', 'Martinique', 'Nicaragua', 'Panama', 'Jamaica', 'Bahamas', 'Barbados', 'Dominica']
juzna_amerika = ['Brazil', 'Argentina', 'Bolivia', 'Chile', 'Colombia', 'Ecuador', 'Falkland Islands', 'French Guiana', 'Guyana', 'Paraguay', 'Peru', 'South Georgia', 'South Sandwich Islands', 'Suriname', 'Trinidad and Tobago', 'Uruguay', 'Venezuela']
amerika = severna_amerika + juzna_amerika
oceanija = ['Australia', 'Fiji', 'New Zealand', 'Federated States of Micronesia', 'Kiribati', 'Marshall Islands', 'Nauru', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']

# funkcije
def prenesi(datoteka):
    '''prenese izbrani csv in vrne tabelo katere elementi so vrstice iz csv-ja'''
    igre = []
    with open(datoteka, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        _ = next(csvreader)
        for row in csvreader:
            igre.append(row)
    return igre

def najdi_drzave(tab_drzav, izbrane_igre):
    '''tab_drzav - tabela samo držav, izbrane_igre - tabela držav in medalj,
        vrne tabelo skupnih držav z njihovimi medaljami'''
    tabela = []
    for el1 in tab_drzav:
        for el2 in sorted(izbrane_igre):
            if el1.strip().lower() == el2[0].lower():
                tabela.append(el2)
    return tabela

def malo_statistike(tabela_drzav, i):
    '''prejme tabelo tabel z državo in številom medalj ter indeks i, na katerem mestu v tabeli se nahaja izbrana
        medalja katere statistiko želimo. Izpiše malo statistike'''
    najvec_poleti = max(tabela_drzav, key=lambda x: int(x[i]))
    najmanj_poleti = min(tabela_drzav, key=lambda x: int(x[i]))
    print(f'\nNajveč zlatih medalj je na poletnih igrah dosegel/-a {najvec_poleti[0]}:{najvec_poleti[i]}, medtem ko je na zimskih dosegel/-a {najvec_poleti[i+4]}.')
    print(f'Najmanj zlatih medalj je na poletnih igrah dosegel/-a {najmanj_poleti[0]}: {najmanj_poleti[i]}, medtem ko je na zimskih dosegel/-a {najmanj_poleti[i+4]}.')
    najvec_zima = max(tabela_drzav, key=lambda x: int(x[i+4]))
    najmanj_zima = min(tabela_drzav, key=lambda x: int(x[i+4]))
    print(f'\nNajveč zlatih medalj je na zimskih igrah dosegel/-a {najvec_zima[0]}: {najvec_zima[i+4]}, medtem ko je na poletnih dosegel/-a {najvec_zima[i]}.')
    print(f'Najmanj zlatih medalj je na zimskih igrah dosegel/-a {najmanj_zima[0]}:{najmanj_zima[i+4]}, medtem ko je na poletnih dosegel/-a {najmanj_zima[i]}.')


def narisi1(drzave, medalje):
    '''prejme tabelo držav z medaljami(4) in izbrano medaljo ter nariše tabelo'''
    print('\n                       Država | št. medalj na poletnih igrah')
    print('-------------------------------------------------------------')
    for i in range(0, len(drzave)):
        print(f'{drzave[i]:>29s} | {medalje[i]:<28n}')

def narisi2(drzave, medalje1, medalje2):
    '''prejme tabelo držav z medaljami(8) in izbrano medaljo ter nariše tabelo'''
    print('\n            Država            | št. medalj na poletnih igrah | št. medalj na zimskih igrah')
    print('-------------------------------------------------------------------------------------------')
    for i in range(0, len(drzave)):
        print(f'{drzave[i]:^29s} | {medalje1[i]:^28n} | {medalje2[i]:^28n}')

# PROGRAM
        
# izpišemo nekaj osnovnih podatkov o olimpisjkih igrah
tab_vseh = prenesi('vse_olimpijske.csv')
print('OLIMPISJKE IGRE')
st_vseh_medalj = sum([int(tab_vseh[i][4]) for i in range(len(tab_vseh))])
print(f'Do sedaj je na olimpijskih igrah doseglo {len(tab_vseh)} držav katerokoli od {st_vseh_medalj} medalj.')
print(f'Največ zlatih medalj je prejel/-a {max(tab_vseh, key=lambda x: int(x[1]))[0]}, srebrnih {max(tab_vseh, key=lambda x: int(x[2]))[0]} in bronastih {max(tab_vseh, key=lambda x: int(x[3]))[0]}.')

# izberemo igre ki jih želimo analizirat in prenesemo njihov csv
igra = input('\nKatere olimpijske igre želite primerjati med seboj? Napišite eno od možnosti: poletne/zimske/vse/primerjava poletnih in zimskih: ')
while True:
    if igra == 'poletne':
        izbrane_igre = prenesi('poletne_olimpijske.csv')
        barva = '#f9d62e' # to potrebujemo kasneje za grafikon
        break
    elif igra == 'zimske':
        izbrane_igre = prenesi('zimske_olimpijske.csv')
        barva = '#bae1ff'
        break
    elif igra == 'vse':
        izbrane_igre = prenesi('vse_olimpijske.csv')
        barva = '#a3ceb1'
        break
    elif igra == 'primerjava poletnih in zimskih':
        izbrane_igre = prenesi('pz_olimpijske.csv')
        break
    else:
        igra = input('teh iger ne poznamo, poskusite ponovno: ')

# tabele v 'primerjava poletnih in zimskih' imajo 9 elementov, medtem ko jih imajo ostale 5,
# zato to tabelo obravnavamo posebaj
if igra != 'primerjava poletnih in zimskih':
    
    # uprašamo uporabnika katere države želi primerjati med seboj
    # uporabnik lahko izbere med primerjavo držav določene celine ali pa države ročno vpiše
    izbrane_drzave = input('\nKatere države želite primerjati med seboj? Napišite posamezno državo (v angleščini) ali izberite eno od možnosti: Afrika/Azija/Severna Amerika/Južna Amerika/Evropa/Oceanija: ')
    tabela = []
    while True:
        if izbrane_drzave == 'Evropa':
            tabela = najdi_drzave(evropa, izbrane_igre)
            break
        elif izbrane_drzave == 'Azija':
            tabela = najdi_drzave(azija, izbrane_igre)
            break
        elif izbrane_drzave == 'Afrika':
            tabela = najdi_drzave(afrika, izbrane_igre)
            break
        elif izbrane_drzave == 'Severna Amerika':
            tabela = najdi_drzave(severna_amerika, izbrane_igre)
            break
        elif izbrane_drzave == 'Južna Amerika':
            tabela = najdi_drzave(juzna_amerika, izbrane_igre)
            break
        elif izbrane_drzave == 'Amerika':
            tabela = najdi_drzave(amerika, izbrane_igre)
            break
        elif izbrane_drzave == 'Oceanija':
            tabela = najdi_drzave(oceanija, izbrane_igre)
            break
#         elif izbrane_drzave == 'Antarktika' or izbrane_drzave == 'antarktika':
#             print('\npingvini so zmagali vse igre in dobili vse medalje')
#             tabela = [['ljudje', 0, 0, 0, 0],['pingvini', 1, 1, 1, 1]]
#             plt.xticks([0,1], ('nič','vse'))
#             break
        else:
            # če uporabnik ročno vpiše države, preverimo ali so v načem csv-ju in jih dodamo v tabelo
            # v nasprotnem primeru prosimo naj napiše države še enkrat
            for el1 in sorted(izbrane_drzave.split(',')):
                for el2 in sorted(izbrane_igre):
                    if el1.strip().lower() == el2[0].lower():
                        tabela.append(el2)
            if len(izbrane_drzave.split(',')) != len(tabela):
                tab_drzav = [i[0].lower() for i in tabela]
                for el in izbrane_drzave.split(','):
                    if el.strip().lower() not in tab_drzav:
                        tabela = []
                        print(f'{el} ne obstaja ali pa še ni dosegel/-a medalje na nobenih olimpijskih igrah ', end='')
                        izbrane_drzave = input('napišite izbrane drzave še enkrat: ')
            else:
                break
    
    drzava, zlata, srebrna, bronasta, skupaj = [], [], [], [], []
    for el in sorted(tabela):
        drzava.append(el[0])
        zlata.append(int(el[1]))
        srebrna.append(int(el[2]))
        bronasta.append(int(el[3]))
        skupaj.append(int(el[4]))

    # uporabnika vprašamo katere medalje želi primerjati med seboj
    # sproti izpišemo še nekaj statistike in tabelo z državami in številom medalj
    medalja = input('\nKatere medalje želite primerjati med seboj? Napišite eno od možnosti: zlata/srebrna/bronasta/vse: ')
    while True:
        if medalja == 'zlata':
            print(f'\nNajveč zlatih medalj je dosegel/-a {max(tabela, key=lambda x: int(x[1]))[0]}')
            print(f'Najmanj zlatih medalj je dosegel/-a {min(tabela, key=lambda x: int(x[1]))[0]}')
            narisi1(drzava, zlata) # se nariše tabela
            plt.title('primerjava držav glede na število doseženih zlatih medalj') # naslov grafikona za kasneje
            H = zlata # os od grafikona za kasneje
            break
        elif medalja == 'srebrna':
            print(f'\nNajveč srebrnih medalj je dosegel/-a {max(tabela, key=lambda x: int(x[2]))[0]}')
            print(f'Najmanj srebrnih medalj je dosegel/-a {min(tabela, key=lambda x: int(x[2]))[0]}')
            narisi1(drzava, srebrna)
            plt.title('primerjava držav glede na število doseženih srebrnih medalj')
            H = srebrna
            break
        elif medalja == 'bronasta':
            print(f'\nNajveč bronastih medalj je dosegel/-a {max(tabela, key=lambda x: int(x[3]))[0]}')
            print(f'Najmanj bronastih medalj je dosegel/-a {min(tabela, key=lambda x: int(x[3]))[0]}')
            narisi1(drzava, bronasta)
            plt.title('primerjava držav glede na število doseženih bronastih medalj')
            H = bronasta
            break
        elif medalja == 'vse':
            print(f'\nNajveč medalj je dosegel/-a {max(tabela, key=lambda x: int(x[1]))[0]}')
            print(f'Najmanj medalj je dosegel/-a {min(tabela, key=lambda x: int(x[1]))[0]}')
            narisi1(drzava, skupaj)
            plt.title('primerjava držav glede na število doseženih medalj')
            H = skupaj
            break
        else:
            medalja = input('te medalje ne poznamo, poskusite ponovno: ')
            
    # narišemo grafikon
    X = drzava
    plt.barh(X, H, color = barva)
    plt.xlabel('število medalj')
    plt.ylabel('države')
    plt.show()
            
else:
    # uprašamo uporabnika katere države želi primerjati med seboj
    # uporabnik lahko izbere med primerjavo držav določene celine ali pa države ročno vpiše
    izbrane_drzave = input('\nKatere države želite primerjati med seboj? Napišite posamezno državo (v angleščini) ali izberite eno od možnosti: Afrika/Azija/Severna Amerika/Južna Amerika/Evropa/Oceanija: ')
    tabela = []
    while True:
        if izbrane_drzave == 'Evropa':
            tabela = najdi_drzave(evropa, izbrane_igre)
            break
        elif izbrane_drzave == 'Azija':
            tabela = najdi_drzave(azija, izbrane_igre)
            break
        elif izbrane_drzave == 'Afrika':
            tabela = najdi_drzave(afrika, izbrane_igre)
            break
        elif izbrane_drzave == 'Severna Amerika':
            tabela = najdi_drzave(severna_amerika, izbrane_igre)
            break
        elif izbrane_drzave == 'Južna Amerika':
            tabela = najdi_drzave(juzna_amerika, izbrane_igre)
            break
        elif izbrane_drzave == 'Amerika' or izbrane_drzave == 'amerika':
            tabela = najdi_drzave(amerika, izbrane_igre)
            break
        elif izbrane_drzave == 'Oceanija':
            tabela = najdi_drzave(oceanija, izbrane_igre)
            break
#         elif izbrane_drzave == 'Antarktika' or izbrane_drzave == 'antarktika':
#             print('pingvini so dosegli vse medalje')
#             tabela = [['ljudje', 0, 0, 0, 0, 0, 0, 0, 0],['pingvini', 1, 1, 1, 1, 1, 1, 1, 1]]
#             break
        else:
            # če uporabnik ročno vpiše države, preverimo ali so v načem csv-ju in jih dodamo v tabelo
            # v nasprotnem primeru prosimo naj napiše države še enkrat
            for el1 in sorted(izbrane_drzave.split(',')):
                for el2 in sorted(izbrane_igre):
                    if el1.strip().lower() == el2[0].lower():
                        tabela.append(el2)
            if len(izbrane_drzave.split(',')) != len(tabela):
                tab_drzav = [i[0].lower() for i in tabela]
                for el in izbrane_drzave.split(','):
                    if el.strip().lower() not in tab_drzav:
                        tabela = []
                        print(f'{el} ne obstaja ali pa še ni dosegel/-a medalje na nobenih olimpijskih igrah ', end='')
                        izbrane_drzave = input('napišite izbrane drzave še enkrat: ')
            else:
                break
    
    drzava, pzl, psr, pbr, psk, zzl, zsr, zbr, zsk = [], [], [], [], [], [], [], [], []
    for el in sorted(tabela):
        drzava.append(el[0])
        pzl.append(int(el[1]))
        psr.append(int(el[2]))
        pbr.append(int(el[3]))
        psk.append(int(el[4]))
        zzl.append(int(el[5]))
        zsr.append(int(el[6]))
        zbr.append(int(el[7]))
        zsk.append(int(el[8]))
    
    # uporabnika vprašamo katere medalje želi primerjati med seboj
    # sproti izpišemo še nekaj statistike in tabelo z državami in številom medalj
    medalja = input('\nKatere medalje želite primerjati med seboj? Napišite eno od možnosti: zlata/srebrna/bronasta/vse: ')
    while True:
        if medalja == 'zlata':
            malo_statistike(tabela, 1) # funkcija ki izpiše nekaj statistike
            df = pd.DataFrame({'poletne': pzl, 'zimske': zzl}, index=drzava)
            narisi2(drzava, pzl, zzl) # nariše tabelo
            break
        elif medalja == 'srebrna':
            malo_statistike(tabela, 2)
            df = pd.DataFrame({'poletne': psr, 'zimske': zsr}, index=drzava)
            narisi2(drzava, psr, zsr)
            break
        elif medalja == 'bronasta':
            malo_statistike(tabela, 3)
            df = pd.DataFrame({'poletne': pbr, 'zimske': zbr}, index=drzava)
            narisi2(drzava, pbr, zbr)
            break
        elif medalja == 'vse':
            malo_statistike(tabela, 4)
            df = pd.DataFrame({'poletne': psk, 'zimske': zsk}, index=drzava)
            narisi2(drzava, psk, zsk)
            break
        else:
            medalja = input('te medalje ne poznamo, poskusite ponovno: ')
    
    # narišemo grafikon
    ax = df.plot.barh(rot=0, color={'poletne': '#f9d62e', 'zimske': '#bae1ff'})
    plt.xlabel('število medalj')
    plt.ylabel('države')
    plt.title('primerjava držav na poletnih in zimskih igrah')
    plt.show()

