from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Paired12
import json
import itertools

def DisplayData(JsonFile):
    try:
        with open(JsonFile,'r') as openfile:
            json_obj = json.load(openfile)
        print('Json File Successfully Loaded')
    except:
        print('ERROR! File failed to load!')
        return -1

    Countries = []
    Deaths = []
    NormalizedDeaths = []

    for element in json_obj:
        Countries.append(element['Country'])
        Deaths.append(element['Total Deaths'])
        NormalizedDeaths.append(element['Normalized Deaths'])

    newPallet = []
    colors = itertools.cycle(Paired12)
    for i, color in zip(range(len(Countries)), colors):
        newPallet.append(color)
    source = ColumnDataSource(data=dict(Countries = Countries, Deaths = Deaths,color = newPallet))
    p = figure(x_range=Countries, height=700, title="Culmulative Deaths", width = 1400, tools = "box_zoom,reset")
    p.vbar(x='Countries', top= 'Deaths', width=.7, color = "color", source = source)
    p.xaxis.major_label_orientation = "vertical"
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    show(p)


    
    



