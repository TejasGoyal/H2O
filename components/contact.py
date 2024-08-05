from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app

def create_contact():
    return dbc.Container([
        html.H2("Contact"),
        dbc.Row([
            dbc.Col([
                dbc.Label("Name"),
                dbc.Input(id='name-input', type='text'),
            ]),
            dbc.Col([
                dbc.Label("Email"),
                dbc.Input(id='email-input', type='email'),
            ]),
        ]),
        dbc.Label("Message"),
        dbc.Textarea(id='message-input'),
        dbc.Button("Send", id='send-button', color='primary'),
        html.Div(id='contact-output')
    ])

@app.callback(
    Output('contact-output', 'children'),
    [Input('send-button', 'n_clicks')],
    [dash.dependencies.State('name-input', 'value'),
     dash.dependencies.State('email-input', 'value'),
     dash.dependencies.State('message-input', 'value')]
)
def update_contact(n_clicks, name, email, message):
    if n_clicks is None:
        return ""
    # This is where you would typically handle sending the message, e.g., via an email API
    return "Thank you for your message!"
