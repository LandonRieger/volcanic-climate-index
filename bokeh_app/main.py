from bokeh.io import curdoc, show
from bokeh.layouts import column, gridplot, row
from bokeh.models import ColumnDataSource, LinearColorMapper, ColorBar, Patch, RangeTool, Range1d, Label, Legend, HoverTool
from bokeh.models.widgets import Div
from bokeh.plotting import figure, output_file
import xarray as xr
import pandas as pd
import numpy as np
import os
from vci_text import vci_text
# output_file("test.html")


def calc_vci():
    aod = global_aod_diff.sel(time=slice(date_to_str(range_tool.x_range.start),
                                         date_to_str(range_tool.x_range.end)))
    vci = aod.integrate(dim='time', datetime_unit='D').values * 365
    top = vci - xr.concat([aod.isel(time=0), aod.isel(time=-1)], dim='time') \
                                                .integrate(dim='time', datetime_unit='D').values * 365

    if top <= 0:
        return 0
    else:
        return np.log10(top)


def date_to_str(date):
    try:
        return str(pd.Timedelta(date, 'ms') + pd.Timestamp('1970'))
    except:
        return str(date)


def vci_callback(attr, old, new):
    label2.text = f'VCI: {calc_vci():.2f}'
    label2.x = np.datetime64(date_to_str(range_tool.x_range.end))
    aod_band_diff2.data = calc_aod_in_period().data


def calc_aod_in_period():
    aod_sel = global_aod_diff.sel(time=slice(date_to_str(range_tool.x_range.start),
                                             date_to_str(range_tool.x_range.end)))
    good = aod_sel > 0
    upper = aod_sel.values[(good,)].flatten()
    aod_time = aod_sel.time.values[(good,)].flatten()
    return ColumnDataSource({'time': aod_time, 'aod_fill': upper})


volcanoes = {'El Chichon': (np.datetime64('1982-04-03'), 17.21, -93.13, 5),
             'Nevado del Ruiz': (np.datetime64('1985-10-11'), 4.53, -79.19, 3),
             'Pinatubo': (np.datetime64('1991-06-15'), 15.08, 120.21, 6),
             'Ruang': (np.datetime64('2002-09-25'), 2.3, 125.37, 4),
             'Reventador': (np.datetime64('2002-11-02'), -0.4, -39.21, 4),
             'Manam': (np.datetime64('2005-01-28'), -4.1, 145, 4),
             'Soufriere Hills': (np.datetime64('2006-05-20'), 16.43, -62.11, 3),
             'Rabaul': (np.datetime64('2006-10-07'), -4.14, 152.12, 4),
             'Okmok': (np.datetime64('2008-07-12'), 53.28, -168, 4),
             'Kasatochi': (np.datetime64('2008-08-07'), 52.1, -175, 4),
             'Redoubt': (np.datetime64('2009-03-15'), 60.29, -152.44, 3),
             'Sarychev': (np.datetime64('2009-06-11'), 48.05, 153, 4),
             'Merapi': (np.datetime64('2010-10-25'), -7.32, 110.26, 4),
             'Nabro': (np.datetime64('2011-06-12'), 13.36, 41.69, 4),
             'Puyehue-Cordon': (np.datetime64('2011-06-04'), -40.35, -72.07, 5),
             'Copahue': (np.datetime64('2012-12-23'), 37.51, -71.1, 2),
             'Kelud': (np.datetime64('2014-02-13'), -7.55, 112, 4),
             'Calbuco': (np.datetime64('2015-04-22'), -41.19, -72.37, 4)}

volcanoes = pd.DataFrame.from_dict(volcanoes, orient='index', columns=['time', 'latitude', 'longitude', 'VEI'])
volcanoes.index.name = 'Volcano'

# Compute Aerosol Optical Depth
# compute aod above the tropopause
folder = os.path.dirname(os.path.abspath(__file__))
data = xr.open_dataset(os.path.join(folder, '..', 'data', 'GloSSAC-V1-aod.nc'))
aod = data['Measurements_extinction']

# integrate globally
global_aod = (np.cos(aod.latitude * np.pi / 180) * aod).sum(dim='latitude') \
             / np.cos(aod.latitude * np.pi / 180).sum(dim='latitude')

# compute the 'volcanically perturbed' aod
background = aod.sel(time=slice('1998', '2002')).groupby('time.month').mean(dim='time')
aod_diff = aod.groupby('time.month') - background
global_aod_diff = (np.cos(aod.latitude * np.pi / 180) * aod_diff).sum(dim='latitude') \
                 / np.cos(aod.latitude * np.pi / 180).sum(dim='latitude')

# make the ColumnDataSources for the bokeh plot
df = pd.DataFrame(aod.to_pandas().stack(), columns=['Measurements_extinction']).reset_index()
df['width'] = pd.Timedelta(1, 'M')
source = ColumnDataSource(df)

aod_df = ColumnDataSource({'time': global_aod.time.values, 'aod': global_aod.values})
aod_diff_df = ColumnDataSource({'time': global_aod_diff.time.values, 'aod_diff': global_aod_diff.values})

volc_df = ColumnDataSource(volcanoes)

# ------------------------------------
# plot the latitudinally resolved AOD
# ------------------------------------
p = figure(plot_height=300, plot_width=900,
           x_axis_type='datetime', y_range=(-80, 80),
           x_range=(aod.time.values[0], aod.time.values[-1]), tools="")
mapper = LinearColorMapper(palette='Viridis256', low=0, high=0.01)
rect = p.rect(x="time", y="latitude", width='width', height=np.diff(aod.latitude)[0],
              source=source,
              fill_color={'field': 'Measurements_extinction', 'transform': mapper},
              line_color={'field': 'Measurements_extinction', 'transform': mapper})
p.yaxis.axis_label = "Latitude"
color_bar = ColorBar(color_mapper=mapper,
                     label_standoff=12, border_line_color=None, location=(0, 0))
p.add_layout(color_bar, 'right')

# add the eruption markers
circle = p.circle('time', 'latitude', size=10, color='gray', source=volc_df, name='volcanoes')
hover = HoverTool(tooltips=[("time", "@time{%F}"), ("latitude", "@latitude"),
                            ("Volcano", "@Volcano"), ("VEI", "@VEI"), ],
                  formatters={'time': 'datetime'},
                  renderers=[circle])

p.add_tools(hover)
# ------------------------------------
# plot the globally averaged AOD
# ------------------------------------
p2 = figure(plot_height=300, plot_width=900,
            x_axis_type='datetime', y_axis_type='log',
            y_range=(1e-4, 1e-1), x_range=p.x_range)
a0 = p2.line(x='time', y='aod', source=aod_df, color='gray')
a1 = p2.line(x='time', y='aod_diff', source=aod_diff_df, line_width=1)
p2.yaxis.axis_label = 'Global AOD [1020nm]'

# ------------------------------------
# Add the range tool for selection
# ------------------------------------
range_tool = RangeTool(x_range=Range1d(np.datetime64('1991-05-01'), np.datetime64('1996-06-01')))
range_tool.overlay.fill_color = "gray"
range_tool.overlay.fill_alpha = 0.1

range_tool.x_range.on_change('start', vci_callback)
range_tool.x_range.on_change('end', vci_callback)

p2.ygrid.grid_line_color = None
p2.add_tools(range_tool)
p.add_tools(range_tool)
p2.toolbar.active_multi = range_tool

aod_band_diff2 = calc_aod_in_period()
glyph = Patch(x="time", y="aod_fill", fill_color="#f46842", line_width=0, fill_alpha=0.3)
p2.add_glyph(aod_band_diff2, glyph)

# ------------------------------------
# Add the labels and legends
# ------------------------------------
label2 = Label(y=0.02, x=np.datetime64(date_to_str(range_tool.x_range.end)),
               text=f'VCI: {calc_vci():.2f}',
               text_align='center', text_baseline='middle', text_color='#f46842')
p2.add_layout(label2)

legend = Legend(items=[("Deseasonalized AOD", [a1]), ("Total AOD", [a0])], location="center")
p2.add_layout(legend, 'below')
p2.legend.orientation = "horizontal"

curdoc().title = "Volcanic Climate Index"
curdoc().add_root(column(Div(text='<h1>Volcanic Climate Index</h1>', width=1200),
                         vci_text(width=900),
                         Div(text='<h2>Exploration</h2>', width=900),
                         Div(text='Move the grey shaded area around to determine the VCI for different eruptions. '
                                  'VCI is calculated as the time integrated global aerosol optical depth after the '
                                  'background layer and the baseline value (calculated as the beginning of the period) '
                                  'has been removed. ', width=900),
                         p,
                         p2))
