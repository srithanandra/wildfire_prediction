import xarray as xr
import config

tp_dataset = xr.open_dataset('..\\..\\data\\weather_datasets\\total_precipitation_0_daily-mean.nc')
t2m_dataset = xr.open_dataset('..\\..\\data\\weather_datasets\\2m_temperature_0_daily-mean.nc')
d2m_dataset = xr.open_dataset('..\\..\\data\\weather_datasets\\2m_dewpoint_temperature_stream-oper_daily-mean.nc')

dataset = xr.merge([tp_dataset, t2m_dataset, d2m_dataset], compat='override')

print("Available variables:", list(dataset.data_vars))

dataframe = dataset[['t2m', 'tp']].to_dataframe().reset_index()
dataframe.to_csv(f'{config.RAW_DIR}\\weather.csv', index=False)

print(f"Completed: Data saved to {config.RAW_DIR}\\weather.csv")