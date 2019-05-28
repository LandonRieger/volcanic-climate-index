from bokeh.io import curdoc, output_notebook
from bokeh.themes import Theme
from bokeh.layouts import layout, row, WidgetBox, Spacer
from bokeh.models import ColumnDataSource, LinearColorMapper, ColorBar, Line, Panel
from bokeh.models.widgets import RangeSlider, DateRangeSlider, Dropdown, Toggle
from bokeh.plotting import figure
import xarray as xr
import pandas as pd
import numpy as np

glossac_file = r'C:\Users\lando\data\netcdf\GloSSAC\GloSSAC-V1.nc'
glossac = xr.open_dataset(glossac_file, decode_times=False)

extinction = glossac.Measurements_extinction
extinction = extinction.rename({'altitude1': 'altitude', 'measurement wavelengths': 'ext_wavel'}).sel(ext_wavel=5)
time = pd.date_range('1979', '2016-12-31', freq='MS')
extinction['years'].values = time
extinction = extinction.rename({'years': 'time'})

tropopause = xr.DataArray(np.tile(glossac.trop.values, int(len(glossac.years) / 12)).T,
                          dims=['time', 'latitude'],
                          coords=[extinction.time, extinction.latitude])

aod = extinction.where(extinction.altitude > tropopause).sum(dim='altitude') * 0.5

df = pd.DataFrame(aod.to_pandas().stack(), columns=['extinction']).reset_index()
df['width'] = pd.Timedelta(1, 'M')

output_notebook()
p = figure(plot_height=350, plot_width=600, tooltips=[("x", "$x"), ("y", "$y"), ("value", "@extinction")],
           x_axis_type='datetime', y_range=(-90, 90))

source = ColumnDataSource(df)
mapper = LinearColorMapper(palette='Viridis256', low=0, high=0.01)
rect = p.rect(x="time", y="altitude", width='width', height=1,
              source=source,
              fill_color={'field': 'extinction', 'transform': mapper},
              line_color={'field': 'extinction', 'transform': mapper})
p.yaxis.axis_label = "Altitude [km]"

color_bar = ColorBar(color_mapper=mapper,
                     label_standoff=12, border_line_color=None, location=(0, 0))

p.add_layout(color_bar, 'right')