import os
import dash

app = dash.Dash(__name__)
app.layout = dash.html.Div(children=[dash.html.H1(f'Mon projet {os.getenv("MODEL_API")}')])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8888)
