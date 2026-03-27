import pandas as pd
from pathlib import Path

def main():
    project_root = Path(__file__).resolve().parents[2]
    output_path = project_root / "data" / "raw" / "fires.csv"
    url = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6.1/csv/MODIS_C6_1_USA_contiguous_and_Hawaii_24h.csv'
    fires = pd.read_csv(url)
    fires = fires[['latitude', 'longitude', 'acq_date']]
    fires.to_csv(output_path, index=False)
    print(f'Completed: Data saved to fires.csv in data\\raw')