# Load the packages
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# read the data, set the index
bank = pd.read_excel("F:/GoogleDrive/python/bank.xlsx", index_col=0)
bank = bank.sort_index(axis=1)
# bank.head(2)

# get the x axis labels, ie the bank names
bank_names = bank.columns.tolist()
# bank_names

# get the data frame index for x axis
variable = bank.index.tolist()
#len(variable)

# get the color list
col_ind=np.array(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",  "#9467bd",  "#8c564b",  "#e377c2",  "#7f7f7f",  "#bcbd22",  "#17becf" ])
col_ind=np.array(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",  "#9467bd",  "#8c564b",  "#e377c2",  "#7f7f7f",  "#bcbd22",  "#17becf" ])
col_ind=np.tile(col_ind, 3)
col_ind=col_ind.tolist()[0:len(variable)]
#len(col_ind)
#len(col_ind)

# initiate the app
app = dash.Dash()

# set the layout
app.layout = html.Div(
    [
        html.H1(children="Banking Information", style={"textAlign": "center"}),
        html.H3(children="As on 31-12-2019", style={"textAlign": "center"}),
        #html.Div(children="As on 31-12-2019", style={"textAlign": "center", 'fontsize':'50px'}),
        #html.Label("Choose a Variable"),
        dcc.Dropdown(
            id="Select Variable", 
            options=[
        {'label': i, 'value': i} for i in variable
    ], value= variable[0], clearable=False,
        style={"display": "block",'fontSize' : '20px', "margin-left": "auto",
                                        "margin-right": "auto", "width": "60%"}),
        dcc.Graph(
            id="FinIndic"
        )
    ]
)

# app callback
@app.callback(Output("FinIndic", "figure"),[Input("Select Variable", "value")])

# set the function for plot
def financial_indicator(selected_value):
    Y = bank.loc[bank.index==selected_value]
    Y=Y.values.tolist()[0]
    ind=variable.index(selected_value)
    trace=go.Bar(x=bank_names, y=Y, marker={'color':col_ind[ind]})
    return {
        'data': [trace]}
    
# launch the app
if __name__ == "__main__":
    app.run_server(port=4050)

