import xarray as xr
from src.config import RAW_DIR
import cdsapi

# ds = xr.open_dataset('era5_daily.nc')
# df = ds[['t2m', 'u10', 'v10', 'tp']].to_dataframe().reset_index()
# df.to_csv(f'{RAW_DIR}/weather.csv', index=False)