import xarray as xr
from src.config import RAW_DIR

ds = xr.open_dataset('modis_ndvi.nc')
df = ds.to_dataframe().reset_index()
df.to_csv(f'{RAW_DIR}/ndvi.csv', index=False)
