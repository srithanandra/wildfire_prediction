import xarray as xr
import cdsapi

RAW_DIR = 'data/raw'
dataset = xr.open_dataset('C:\\Users\\andra\\Downloads\\weather_datasets\\total_precipitation_0_daily-mean.nc') # download this dataset
dataframe = dataset[['t2m', 'u10', 'v10', 'tp']].to_dataframe().reset_index()
dataframe.to_csv(f'{RAW_DIR}/weather.csv', index=False)