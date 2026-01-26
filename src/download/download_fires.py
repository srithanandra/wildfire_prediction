import pandas as pd

RAW_DIR = 'data/raw'

url = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6.1/csv/MODIS_C6_1_USA_contiguous_and_Hawaii_24h.csv'
fires = pd.read_csv(url)
fires = fires[['latitude', 'longitude', 'acq_date']]
fires.to_csv(f'{RAW_DIR}/fires.csv', index=False)
print('completed')