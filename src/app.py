import dash
import dash_bootstrap_components as dbc

import layout
from mlflow_model_client import predict

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row(dbc.Col(layout.title, width=6)),
    dbc.Row([dbc.Col(layout.model_inputs, width=3), dbc.Col(layout.model_output, width=3)]),
], fluid=True)


@app.callback(
    dash.Output(component_id='model_output', component_property='value'),
    dash.Input(component_id='x1', component_property='value'),
    dash.Input(component_id='x2', component_property='value'),
    dash.Input(component_id='x3', component_property='value')
)
def update_model_output(x1, x2, x3):
    return predict(x=[x1, x2, x3])


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8888, debug=True)
