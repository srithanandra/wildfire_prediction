import pandas as pd
from pathlib import Path
import sqlite3

def main():
    project_root = Path(__file__).resolve().parents[2]
    output_path = project_root / "data" / "raw" / "fires.db"
    url = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6.1/csv/MODIS_C6_1_USA_contiguous_and_Hawaii_24h.csv'
    fires = pd.read_csv(url)
    fires = fires[['latitude', 'longitude', 'acq_date']]

    conn = sqlite3.connect(output_path)
    try:
        fires.to_sql("fires", conn, if_exists="replace", index=False)
    finally:
        conn.close()

    print('Completed: Data saved to fires.db in data\\raw')