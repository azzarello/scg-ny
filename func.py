import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime


def generate_crime_entry(num):
    ret = []
    for i in range(int(num)):
        ret.append(crime_entry_div(i))
    return ret


def crime_entry_div(offense_no):
    return html.Div(children=[
        html.P(children='Disposition'),
        dcc.RadioItems(id=('disposition-dropdown-' + str(offense_no)), options=[
            {'label': 'Guilty', 'value': 'Guilty'},
            {'label': 'Not Guilty', 'value': 'Not Guilty'},
            {'label': 'Dismissed', 'value': 'Dismissed'},
        ],
            value='Guilty'
        ),

        html.P(children='What is the date of disposition?'),
        dcc.DatePickerSingle(
            id=('date-disposition-'+str(offense_no)),
            date=datetime(2010, 1, 1)
        ),

        html.P(children='Have you completed your sentence?'),
        dcc.RadioItems(
            options=[
                {'label': 'Yes', 'value': 'YES'},
                {'label': 'No', 'value': 'NO'},
            ],
            value='YES',
            id=('sentence-completion-'+str(offense_no))
        ),

        html.P(children='What is the date of sentence completion?'),
        dcc.DatePickerSingle(
            id=('date-completion'+str(offense_no)),
            date=datetime(2020, 1, 1)
        )])
