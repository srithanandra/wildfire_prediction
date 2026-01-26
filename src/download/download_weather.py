import xarray as xr
import cdsapi

RAW_DIR = 'data/raw'
ds = xr.open_dataset('era5_daily.nc') # download this dataset
df = ds[['t2m', 'u10', 'v10', 'tp']].to_dataframe().reset_index()
df.to_csv(f'{RAW_DIR}/weather.csv', index=False)