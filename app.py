import pandas as pd
import flask
import dash
from dash_core_components import Interval, Tabs, Tab, Store, RadioItems, Upload, Dropdown
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

app.layout = html.Div(html.H1(children='Hello Dash'))

if __name__ == '__main__':
    flask_server.run(debug=True)
