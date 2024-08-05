from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

def create_bmi_calculator():
    return dbc.Container([
        html.H2("BMI Calculator"),
        dbc.Row([
            dbc.Col([
                dbc.Label("Height (cm)"),
                dbc.Input(id='height-input', type='number', min=0),
            ]),
            dbc.Col([
                dbc.Label("Weight (kg)"),
                dbc.Input(id='weight-input', type='number', min=0),
            ]),
        ]),
        dbc.Button("Calculate BMI", id='calculate-bmi', color='primary'),
        html.Div(id='bmi-output')
    ])

@app.callback(
    Output('bmi-output', 'children'),
    [Input('calculate-bmi', 'n_clicks')],
    [dash.dependencies.State('height-input', 'value'),
     dash.dependencies.State('weight-input', 'value')]
)
def update_bmi(n_clicks, height, weight):
    if n_clicks is None or height is None or weight is None:
        return ""
    bmi = weight / ((height / 100) ** 2)
    return f"Your BMI is: {bmi:.2f}"
