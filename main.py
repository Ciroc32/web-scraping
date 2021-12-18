from bs4 import BeautifulSoup
import requests # requete (ex : 200)
import os #synchro programme / ordinateur
import csv #tableur modifié avec bash
import re #regex

# récup page html via url
page = requests.get("https://www.data.gouv.fr/fr/reuses/cartographie-dynamique-sur-la-vacance-de-courte-duree-dans-le-parc-prive-par-commune/")
# pour concaténer la page correctement
soup = BeautifulSoup(page.content, 'html.parser')

a = re.findall("[0-9]","Toto123")
print(a)

def csv_parser():
    import csv
    with open("sae.csv", newline='') as csvfile:
        lire = csv.reader(csvfile, delimiter=":", quotechar="|")
        for tableau in lire:
            print(", ".join(tableau))
a = csv_parser().replace(":","||")
print(a)

print(soup.prettify())
print(soup.find_all('p')[0].get_text())