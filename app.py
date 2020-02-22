import pandas as pd
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import base64
from io import StringIO
from io import BytesIO
import urllib.parse
import datetime
import time
import pickle

from dash.dependencies import Input, Output, State

flask_server = flask.Flask(__name__)
app = dash.Dash(__name__, server=flask_server, url_base_pathname='/')
app.css.append_css(
    {'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})


app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(
    children=html.Div([html.H2(children='The Second Chance Gap - The State of New York', className='nine columns'),
                       dcc.Dropdown(options=[
                           {'label': 'New York City', 'value': 'NYC'},
                           {'label': 'Montréal', 'value': 'MTL'},
                           {'label': 'San Francisco',
                            'value': 'SF'}
                       ],
        value='MTL'),
        dcc.RadioItems(options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),
        dcc.Input(
        placeholder='Enter a value...',
        type='text',
        value=''
    )]))

if __name__ == '__main__':
    flask_server.run(debug=True)
