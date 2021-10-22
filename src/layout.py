import os

import dash_bootstrap_components as dbc
from dash.html import H3

title = H3('Dash & MLflow', style={'textAlign': 'center'}),

model_inputs = dbc.Card([
    dbc.CardHeader('Model inputs'),
    dbc.CardBody([
        dbc.InputGroup([
            dbc.Input(id="x1", type='number', placeholder="X1", value=0, style={'width': '33%'}),
            dbc.Input(id="x2", type='number', placeholder="X1", value=0, style={'width': '33%'}),
            dbc.Input(id="x3", type='number', placeholder="X1", value=0, style={'width': '33%'})]
        ),
        dbc.FormText("Enter value of model inputs: X1, X2, X3")
    ])
], className='mt-2 mb-3')

model_output = dbc.Card([
    dbc.CardHeader('Model output'),
    dbc.CardBody([
        dbc.Input(value='No prediction.', id='model_output', className='text-primary', disabled=True),
        dbc.FormText(f"MLflow prediction API at {os.getenv('MODEL_API')}")
    ])
], className='mt-2 mb-3')
