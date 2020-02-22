import pandas as pd
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime

from dash.dependencies import Input, Output, State

from func import crime_entry_div, generate_crime_entry

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

flask_server = flask.Flask(__name__)
app = dash.Dash(__name__, server=flask_server,
                url_base_pathname='/',
                external_stylesheets=external_stylesheets)


app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
    html.Div(html.H2(
        children='The Second Chance Gap', className='nine columns')),

    html.Div(children=[
        dcc.Dropdown(id='state-dropdown',
                     options=[
                         {'label': 'New York', 'value': 'NY'},
                         {'label': 'Washington State',
                          'value': 'WA'}
                     ],
                     value='NY',
                     className='six columns'),
        dcc.Input(
            placeholder='Enter the number of crimes committed...',
            type='number',
            value='0',
            id='crimes-committed-input'
        )]),

    html.Div(id='charges-div', children=generate_crime_entry(2))
])


@app.callback(Output('charges-div', 'children'),
              [Input('crimes-committed-input', 'value')])
def generate_case_entry_div(value):
    return generate_crime_entry(value)


@app.callback(Output('output', 'children'),
              [Input('state-dropdown', 'value')])
def update_output_component(dropdown_value):
    return dropdown_value


if __name__ == '__main__':
    flask_server.run(debug=True)
