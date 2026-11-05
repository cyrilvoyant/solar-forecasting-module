"""Build data/ajaccio_ghi_1998-2008.csv from Meteo-France open data.

Source: Meteo-France, "Donnees climatologiques de base - horaires", department 20 (Corsica),
https://www.data.gouv.fr/fr/datasets/donnees-climatologiques-de-base-horaires/
Licence Ouverte / Open Licence 2.0 (Etalab).

Station 20004002 (AJACCIO). Hourly global radiation in J/cm2:
- 1998-2007: column GLO2 (hour in true solar time, TSV); GLO (UTC) is empty for these years;
- 2008: column GLO (hour in UTC).
This is the series used in the course (file GLO_ajaccio.txt).
Wh/m2 = J/cm2 / 0.36.

Usage: python make_ajaccio_csv.py
"""
import csv
import gzip
import io
import urllib.request

BASE = "https://meteofrance.s3.sbg.io.cloud.ovh.net/data/synchro_ftp/BASE/HOR/"
FILES = ["H_20_1990-1999.csv.gz", "H_20_2000-2009.csv.gz"]
STATION = "20004002"

rows = []
for name in FILES:
    with urllib.request.urlopen(BASE + name) as resp:
        text = io.TextIOWrapper(gzip.GzipFile(fileobj=io.BytesIO(resp.read())), encoding="utf-8")
        reader = csv.reader(text, delimiter=";")
        head = next(reader)
        ix = {k: i for i, k in enumerate(head)}
        for row in reader:
            if row[ix["NUM_POSTE"]] != STATION:
                continue
            date = row[ix["AAAAMMJJHH"]]
            year = date[:4]
            if "1998" <= year <= "2007":
                value, ref = row[ix["GLO2"]], "TSV"
            elif year == "2008":
                value, ref = row[ix["GLO"]], "UTC"
            else:
                continue
            rows.append((date, value, ref))

rows.sort()
with open("ajaccio_ghi_1998-2008.csv", "w", newline="", encoding="utf-8") as out:
    w = csv.writer(out, delimiter=";")
    w.writerow(["AAAAMMJJHH", "GHI_J_cm2", "hour_reference"])
    w.writerows(rows)
print(len(rows), "hours written")
