from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource,TabPanel,Tabs,CustomJS, Dropdown, MultiChoice
from bokeh.palettes import Paired12
from bokeh.layouts import column, row
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
    DailyDeaths = []

    for element in json_obj:
        Countries.append(element['Country'])
        Deaths.append(element['Total Deaths'])
        NormalizedDeaths.append(element['Normalized Deaths'])
        DailyDeaths.append(element['New Deaths'])
        
    newPallet = []
    colors = itertools.cycle(Paired12)
    for i, color in zip(range(len(Countries)), colors):
        newPallet.append(color)
    source = ColumnDataSource(data=dict(Countries = Countries, Deaths = Deaths, NormalizedDeaths = NormalizedDeaths,DailyDeaths = DailyDeaths,color = newPallet))
    p1 = figure(x_range=Countries, height=700, title="Culmulative Deaths", width = 1400, tools = "box_zoom,reset")
    p1.vbar(x='Countries', top= 'Deaths', width=.7, color = "color", source = source)
    p1.xaxis.major_label_orientation = "vertical"
    p1.xgrid.grid_line_color = None
    p1.y_range.start = 0
    
    tab1 = TabPanel(child=p1, title = "Culmulative Death Totals")

    #----------------------------------------------------------------------------------------------
    

    newPallet = []
    colors = itertools.cycle(Paired12)
    for i, color in zip(range(len(Countries)), colors):
        newPallet.append(color)
    #source = ColumnDataSource(data=dict(Countries = Countries, NormalizedDeaths = NormalizedDeaths,color = newPallet))
    p2 = figure(x_range=Countries, height=700, title="Normalized Deaths", width = 1400, tools = "box_zoom,reset")
    p2.vbar(x='Countries', top= 'NormalizedDeaths', width=.7, color = "color", source = source)
    p2.xaxis.major_label_orientation = "vertical"
    p2.xgrid.grid_line_color = None
    p2.y_range.start = 0

    tab2 = TabPanel(child=p2, title = "Normalized Death Totals")

    #-----------------------------------------------------------------------------------------------

    newPallet = []
    colors = itertools.cycle(Paired12)
    for i, color in zip(range(len(Countries)), colors):
        newPallet.append(color)
    #source = ColumnDataSource(data=dict(Countries = Countries, DailyDeaths = DailyDeaths,color = newPallet))
    p3 = figure(x_range=Countries, height=700, title="Daily Deaths", width = 1400, tools = "box_zoom,reset")
    p3.vbar(x='Countries', top= 'DailyDeaths', width=.7, color = "color", source = source)
    p3.xaxis.major_label_orientation = "vertical"
    p3.xgrid.grid_line_color = None
    p3.y_range.start = 0

    tab3 = TabPanel(child=p3, title = "Daily Death Totals")


    show(Tabs(tabs = [tab1,tab2,tab3]))

    #-----------------------------------------------------------------------------------------------
   



    
    



