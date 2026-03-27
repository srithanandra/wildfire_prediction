import xarray as xr
from pathlib import Path

def main():
    project_root = Path(__file__).resolve().parents[2]
    data_dir = project_root / "data"

    tp_dataset = xr.open_dataset(data_dir / "weather_datasets" / "total_precipitation_0_daily-mean.nc")
    t2m_dataset = xr.open_dataset(data_dir / "weather_datasets" / "2m_temperature_0_daily-mean.nc")
    d2m_dataset = xr.open_dataset(data_dir / "weather_datasets" / "2m_dewpoint_temperature_stream-oper_daily-mean.nc")

    dataset = xr.merge([tp_dataset, t2m_dataset, d2m_dataset], compat='override')

    print("Available variables:", list(dataset.data_vars))

    dataframe = dataset[['t2m', 'tp']].to_dataframe().reset_index()
    dataframe.to_csv(data_dir / "raw" / "weather.csv", index=False)

    print(f"Completed: Data saved to weather.csv")