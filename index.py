import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
from navbar import navbar
from spotipush import spotipush_layout
from app import app

#difference2
nav = navbar()

app.layout = html.Div([
    html.Div(nav),
    html.Div(id="content"),
    dcc.Store(id='rev-button-session', storage_type='session'),
    dcc.Interval(
                id="interval-component",
                interval=2 * 1000,  # in milliseconds
                n_intervals=50,  # start at batch 50
                disabled=False,
            ),
    html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ]),
])

# create callback for modifying page layout
@app.callback(Output("content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return spotipush_layout
    if pathname == "/spotipush":
        return spotipush_layout
    # if not recognised, return 404 message
    return html.P("404 - page not found")


if __name__ == '__main__':
    app.run_server(debug=True, port=8000)

