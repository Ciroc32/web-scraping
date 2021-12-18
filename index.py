#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests # requete (ex : 200)

# récup page html via url
page = requests.get("https://www.data.gouv.fr/fr/reuses/cartographie-dynamique-sur-la-vacance-de-courte-duree-dans-le-parc-prive-par-commune/")
# pour concaténer la page correctement
soup = BeautifulSoup(page.content, 'html.parser')

print(page.content)
# print(soup.prettify())
