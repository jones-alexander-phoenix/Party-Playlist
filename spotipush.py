import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from spotipy_authorization import spt
import dash_bootstrap_components as dbc
from search_box import search_box_layout
from spotipy_authorization import spt
import dash_table
import pandas as pd

def show_tracks(tracks):
    track_list = []
    for i, item in enumerate(tracks['items']):
        track = item['track']
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


def create_spotipush_layout():
    tracks = spt.get_tracks()
    right_card = search_box_layout
    left_card = dbc.Card(
        dbc.CardBody(
            [
                html.Div([
                    html.H4(f'Party Playlist', className='card-title'),
                    html.Div([
                        show_tracks(tracks)
                    ])
                ])
            ]
        ),
        className='w-75',
    )
    row = dbc.Row([
        left_card,
        right_card
    ])
    return row



spotipush_layout = create_spotipush_layout()

if __name__ =='__main__':

    tracks = spt.get_tracks()
    show_tracks(tracks)

