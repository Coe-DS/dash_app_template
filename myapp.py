import plotly.graph_objects as go
import plotly.express as px

import numpy as np

import random, json, time, os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.config.suppress_callback_exceptions = True


#################################################
################# Layout ########################
#################################################

app.layout = html.Div([

    
    html.H1(children='Super Simple Dash App!'),
    html.H2(children='This is an example of a dash app with an interactive dashboard.'),
    
    html.H6("Change below to make a new figure:"),
    
    html.Div([
                "     Number of points, N=: ",
                dcc.Input(id='my-input', value=10, type='number', debounce = True)
              ]),
    
    html.Br(),
     
    dcc.Graph(id='figure-output'),

])

#####################
# Painter Vase Plot #
#####################
    
@app.callback(
    Output('figure-output', 'figure'),
    Input('my-input', 'value'))    
def make_plot(N):
        
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(N), y=np.random.rand(N),
                    mode='lines',
                    name='Random Data'))
                    
    fig.update_layout(title="Model Output")
    
    return fig    
    
    
# -------------------------- MAIN ---------------------------- #


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
