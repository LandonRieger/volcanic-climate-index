import pandas as pd
import holoviews as hv
import xarray as xr
import numpy as np
hv.extension('bokeh')


glossac_file = r'C:\Users\lando\data\netcdf\GloSSAC\GloSSAC-V1.nc'

glossac = xr.open_dataset(glossac_file, decode_times=False)

extinction = glossac.Measurements_extinction
extinction = extinction.rename({'altitude1': 'altitude', 'measurement wavelengths': 'ext_wavel'}).sel(ext_wavel=5)
time = pd.date_range('1979', '2016-12-31', freq='MS')
extinction['years'].values = time
extinction = extinction.rename({'years': 'time'})
# extinction.swap_dims({'time': 'years'})

tropopause = xr.DataArray(np.tile(glossac.trop.values, int(len(glossac.years) / 12)).T,
                          dims=['time', 'latitude'],
                          coords=[extinction.time, extinction.latitude])

aod = extinction.where(extinction.altitude > tropopause).sum(dim='altitude') * 0.5
aod.holoplot()
hv_ds = hv.Dataset(aod)
aod_ds = hv_ds.to(hv.Image, kdims=["time", "latitude"])
aod_ds.opts(colorbar=True, fig_size=200)

fig = hv.render(aod_ds)
fig.show()
print('done')