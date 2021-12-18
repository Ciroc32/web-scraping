import csv
with open("sae.csv", newline='', encoding="utf8") as csvfile:
    lire = csv.reader(csvfile, delimiter=":", quotechar="|")
    for tableau in lire:
        print(", ".join(tableau))
