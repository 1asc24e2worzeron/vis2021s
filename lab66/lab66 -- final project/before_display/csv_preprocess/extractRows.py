import pandas as pd
import json
import csv

with open('night_market.csv', newline='', encoding="utf-8") as csvData:
    rows = csv.reader(csvData)
    with open('night_market_extracted.csv', 'w', newline='', encoding="utf-8") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvHeader = True
        for row in rows:
            if csvHeader:
                csvWriter.writerow(row)
                csvHeader = False
            if (row[5] == '饒河街觀光夜市' or row[5] == '臨江街觀光夜市'):
                csvWriter.writerow(row)

print('Finished.')
