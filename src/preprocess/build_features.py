import pandas as pd
import numpy as np
from src.config import RAW_DIR, PROCESSED_DIR, RADIUS_KM
from src.preprocess.spatial_join import spatial_match

fires = pd.read_csv(f'{RAW_DIR}\\fires.csv')
fires['date'] = pd.to_datetime(fires['acq_date']) + pd.Timedelta(days=1)

weather = pd.read_csv(f'{RAW_DIR}\\weather.csv')
weather['date'] = pd.to_datetime(weather['time'])
weather['temperature'] = weather['t2m'] - 273.15
weather['wind_speed'] = (weather['u10']**2 + weather['v10']**2)**0.5

mask = spatial_match(weather, fires, RADIUS_KM)
weather['label'] = mask.astype(int)

data = weather[['temperature', 'wind_speed', 'tp', 'label']]
data = data.dropna()
data.to_csv(f'{PROCESSED_DIR}\\dataset.csv', index=False)