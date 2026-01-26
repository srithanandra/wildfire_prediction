import xarray as xr

RAW_DIR = 'data/raw'

ds = xr.open_dataset('modis_ndvi.nc') # download this dataset
df = ds.to_dataframe().reset_index()
df.to_csv(f'{RAW_DIR}/ndvi.csv', index=False)