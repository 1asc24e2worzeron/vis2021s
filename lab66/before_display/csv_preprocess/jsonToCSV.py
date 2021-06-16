import pandas as pd
import json

jsonFileName = 'night_market'
firstValue = '調味名稱'

with open(jsonFileName + '.json', encoding="utf-8") as jsonData:
    data = json.load(jsonData)
    print(jsonData)

pandasData = pd.json_normalize(data['result']['results']).set_index(firstValue)
pandasData.to_csv(jsonFileName + '.csv')
