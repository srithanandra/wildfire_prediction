import pandas as pd
from src.preprocess.spatial_join import spatial_match
from src import config
from pathlib import Path

def main():
    project_root = Path(__file__).resolve().parents[2]
    data_dir = project_root / "data"

    fires = pd.read_csv(data_dir / "raw" / "fires.csv")
    fires['date'] = pd.to_datetime(fires['acq_date']) + pd.Timedelta(days=1)

    weather = pd.read_csv(data_dir / "raw" / "weather.csv")
    weather['date'] = pd.to_datetime(weather['valid_time'])
    weather['temperature'] = weather['t2m'] - 273.15

    mask = spatial_match(weather, fires, config.RADIUS_KM)
    weather['label'] = mask.astype(int)

    data = weather[['temperature', 'tp', 'label']]
    data = data.dropna()
    data.to_csv(data_dir / "processed" / "dataset.csv", index=False)