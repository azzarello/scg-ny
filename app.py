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
                       dcc.Dropdown(id='state-dropdown',
                                    options=[
                                        {'label': 'New York', 'value': 'NY'},
                                        {'label': 'Washington State', 'value': 'WA'}
                                    ],
                                    value='NY',
                                    className='six columns'),
                       dcc.RadioItems(options=[
                           {'label': 'New York', 'value': 'NY'},
                           {'label': 'Washington State', 'value': 'WA'}
                       ],
        value='NY',
        className='six columns'
    ),
        dcc.Input(
        placeholder='Enter a value...',
        type='text',
        value=''
    ),
        html.H1(id='output', children="")])
)


@app.callback(Output('output', 'children'),
              [Input('state-dropdown', 'value')])
def update_output_component(dropdown_value):
    return dropdown_value


if __name__ == '__main__':
    flask_server.run(debug=True)
