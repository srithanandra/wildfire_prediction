import xarray as xr
import config

# Open each dataset
tp_dataset = xr.open_dataset('C:\\Users\\andra\\Downloads\\weather_datasets\\total_precipitation_0_daily-mean.nc')
t2m_dataset = xr.open_dataset('C:\\Users\\andra\\Downloads\\weather_datasets\\2m_temperature_0_daily-mean.nc')
d2m_dataset = xr.open_dataset('C:\\Users\\andra\\Downloads\\weather_datasets\\2m_dewpoint_temperature_stream-oper_daily-mean.nc')

# Merge all datasets together (with compat='override' to avoid warning)
dataset = xr.merge([tp_dataset, t2m_dataset, d2m_dataset], compat='override')

# Check what variables are available
print("Available variables:", list(dataset.data_vars))

# Extract the variables you need
dataframe = dataset[['t2m', 'tp']].to_dataframe().reset_index()
dataframe.to_csv(f'{config.RAW_DIR}\\weather.csv', index=False)

print(f"Data saved to {config.RAW_DIR}\\weather.csv")