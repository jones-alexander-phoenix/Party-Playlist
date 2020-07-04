import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
from navbar import navbar
from app import app
from spotipy_authorization import spt
from spotipy_authorization import spt
import dash_table
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint


def show_tracks(tracks):
    track_list = []
    track = tracks['item']
    track_list.append([track['artists'][0]['name'], track['name']])
    df_tracks = pd.DataFrame(track_list, columns=['Artist', 'Track'])
    tracks_table = dash_table.DataTable(
        id='tracks-table',
        columns=[{'name': i, 'id': i} for i in df_tracks.columns],
        data=df_tracks.to_dict('rows'),
        style_cell={
            'height': 'auto',
            'whiteSpace': 'normal'
        },
    )
    return html.Div(tracks_table, style={'display': 'flex', 'justify-content': 'center'})


def search_box():
    search_box_layout = dbc.Card([
            html.H3(f'Current Jam'),
            html.Div(show_tracks(spt.current_track)),
            html.H6("Search for Songs", style={'textAlign': 'left'}),
            dbc.Input(id='search-box-input', placeholder='Enter Text Here'),
            html.Div(id='search-box-output')
    ])
    layout = html.Div([
        dbc.CardGroup([search_box_layout]),
        ],
        className="w-25",
    )
    return layout


search_box_layout = search_box()


@app.callback(
    [Output('search-box-output', 'children')],
    [Input('search-box-input', 'children')]
)
def return_search_results(search_input):
    if search_input:
        result = spt.search(search_input)
    else:
        return "No Song Found"
    print(pprint.pprint(result))
    return "Song Found"
