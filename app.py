import pandas as pd
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime
from pprint import pprint

from dash.dependencies import Input, Output, State

from func import generate_crime_entry, generate_ny_counties, parse_charges, output_answers

external_stylesheets = [
    "https://codepen.io/chriddyp/pen/bWLwgP.css"]

# "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"

flask_server = flask.Flask(__name__)
app = dash.Dash(__name__, server=flask_server,
                url_base_pathname='/',
                external_stylesheets=external_stylesheets)


app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True

ny_counties = generate_ny_counties()


app.layout = html.Div(children=[
    html.Div(html.H2(
        children='The Second Chance Gap'), style={"text-align": "center"}),

    html.Div(children=[

        html.Div(children=[
            html.Div(children=html.P(), className="three columns"),
            html.Div(children=[
                dcc.Dropdown(id='state-dropdown',
                             options=[
                                {'label': 'New York', 'value': 'NY'},
                                {'label': 'Washington State',
                                 'value': 'WA'}
                             ],
                             placeholder='Select State...'),
                html.Br(),
                dcc.Dropdown(id='ny-county-dropdown',
                             options=ny_counties,
                             style={"display": "none"},
                             placeholder='Select County...'
                             ),
            ], className="six columns"),
            html.Div(children=html.P(), className="three columns"), ],
            className="row"
        ),


        html.Br(),

        html.Div(children=[
            html.Div(children=html.P(), className="three columns"),
            html.Div(children=[
                html.P(children='How many crimes did you commit?  ',
                       style={"display": "inline"}),
                dcc.Input(
                    type='number',
                    value=1,
                    id='crimes-committed-input',
                    min=1
                )
            ], className="six columns"),
            html.Div(children=html.P(), className="three columns"), ],
            className="row"
        ),


    ]),


    html.Div(id='charges-div', children=generate_crime_entry(1),
             className="row", style={"text-align": "center"}),




    html.Br(),
    html.Div(children=html.Button('Submit', id='submit-crimes-button',
                                  className="button-primary"), style={"text-align": "center"}),


    html.Hr(),
    html.Div(children=[
        html.H1(children="CONGRATS! You are free now",
                style={"text-align": "center"}, id="result"),
        html.Div(children=[
            html.Div(children=[
                html.P(
                    children="DO YOU HAVE MORE THAN TWO (2) CRIMINAL CONVICTIONS (MISDEMEANOR OR FELONY)?"),
                html.P(children="DO YOU HAVE MORE THAN ONE FELONY CONVICTION?"),
                html.P(
                    children="HAVE LESS THAN TEN YEARS PASSED SINCE YOUR LAST CRIMINAL CONVICTION?"),
                html.P(children="ARE YOU REQUIRED TO REGISTER AS A SEX OFFENDER?"),
                html.P(children="ARE YOU APPLYING TO SEAL AN INELIGIBLE OFFENSE?"),
                html.P(children="DO YOU CURRENTLY HAVE AN OPEN CRIMINAL CASE?"),
            ], className="ten columns"),
            html.Div(children=[
                html.P(
                    children="√", id="criminal_convictions"),
                html.P(children="√", id="felony_conviction"),
                html.P(
                    children="X", id="ten_years_period"),
                html.P(children="√", id="sex_offender"),
                html.P(children="√", id="ineligible_offense"),
                html.P(children="√", id="open_criminal_case"),
            ], className="two columns", style={"text-align": "right"}),
        ], className="row"),
    ], id="eligibility_info", style={'display': 'none'}),


], className="container")


@app.callback(Output('charges-div', 'children'),
              [Input('crimes-committed-input', 'value')])
def generate_case_entry_div(value):
    return generate_crime_entry(value)


@app.callback(Output('ny-county-dropdown', 'style'),
              [Input('state-dropdown', 'value')])
def update_output_component(dropdown_value):
    if dropdown_value == 'NY':
        return {}
    else:
        return {'display': 'none'}

@app.callback([Output('criminal_convictions', 'children'),
               Output('felony_conviction', 'children'),
               Output('ten_years_period', 'children'),
               Output('sex_offender', 'children'),
               Output('ineligible_offense', 'children'),
               Output('open_criminal_case', 'children'),
               Output('result', 'children'),
               Output('eligibility_info', 'style')],
              [Input('submit-crimes-button', 'n_clicks')],
              [State('charges-div', 'children')])

def update_crimes_store(n, charges):
    if n is not None and n >= 1:
        eligible_list, eligible = parse_charges(charges)
        ret = [0, 0, 0, 0, 0, 0]
        return_message = ''
        ret[0], ret[1], ret[2], ret[3], ret[4], ret[5], return_message = output_answers(
            eligible_list, eligible)
        print('Test Output')
        pprint(ret)
        pprint(return_message)
        return ret[0], ret[1], ret[2], ret[3], ret[4], ret[5], return_message, {}
    return "","","","","", "","", {'display':'none'}


if __name__ == '__main__':
    flask_server.run(debug=True)
