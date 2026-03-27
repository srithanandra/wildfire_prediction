import pandas as pd
from src.preprocess.spatial_join import spatial_match
from src import config
from pathlib import Path
import sqlite3
import time

def main():
    project_root = Path(__file__).resolve().parents[2]
    data_dir = project_root / "data"

    raw_dir = data_dir / "raw"
    processed_dir = data_dir / "processed"

    with sqlite3.connect(raw_dir / "fires.db") as conn:
        fires = pd.read_sql_query("SELECT latitude, longitude, acq_date FROM fires", conn)
    fires['date'] = pd.to_datetime(fires['acq_date']) + pd.Timedelta(days=1)

    with sqlite3.connect(raw_dir / "weather.db") as conn:
        weather = pd.read_sql_query("SELECT latitude, longitude, valid_time, t2m, tp FROM weather", conn)
    weather['date'] = pd.to_datetime(weather['valid_time'])
    weather['temperature'] = weather['t2m'] - 273.15

    mask = spatial_match(weather, fires, config.RADIUS_KM)
    weather['label'] = mask.astype(int)

    data = weather[['temperature', 'tp', 'label']]
    data = data.dropna()

    output_db = processed_dir / "dataset.db"
    max_attempts = 5
    for attempt in range(1, max_attempts + 1):
        try:
            with sqlite3.connect(output_db, timeout=30) as conn:
                data.to_sql("dataset", conn, if_exists="replace", index=False)
            break
        except sqlite3.OperationalError as exc:
            if "database is locked" in str(exc).lower() and attempt < max_attempts:
                time.sleep(1.5 * attempt)
                continue
            raise