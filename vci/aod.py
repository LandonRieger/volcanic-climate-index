import xarray as xr
import numpy as np
import pandas as pd


# open the glossac dataset
glossac_file = r'C:\Users\lando\data\netcdf\GloSSAC\GloSSAC-V1.nc'
glossac = xr.open_dataset(glossac_file, decode_times=False)

# read in extinction at 1020nm
extinction = glossac.Measurements_extinction
extinction = extinction.rename({'altitude1': 'altitude',
                                'measurement wavelengths': 'ext_wavel',
                                'years': 'time'})\
                        .sel(ext_wavel=5)

time = pd.date_range('1979', '2016-12-31', freq='MS')
extinction = extinction.assign_coords(time=time, latitude=glossac.lat.values, altitude=extinction.altitude.values)

# tile the tropropause over the entire dataset
tropopause = xr.DataArray(np.tile(glossac.trop.values, int(len(glossac.years) / 12)).T,
                          dims=['time', 'latitude'],
                          coords=[time, glossac.lat.values]).rename('tropopause')

# compute aod above the tropopause
aod = extinction.where(extinction.altitude > tropopause).sum(dim='altitude') * 0.5
xr.merge([aod, tropopause]).to_netcdf('../data/GloSSAC-V1-aod.nc')
