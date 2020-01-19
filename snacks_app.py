# Import the dash packages
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from flask import Flask

import pathlib

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
server = Flask(__name__)

app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

# ---------------------------------------------
# Get the paths
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# ---------------------------------------------


app.layout = html.Div(
    children =[
        html.Div(
            className='row',
            children = [
                html.H1(className='header', children = 'Snacks App'),
                html.Div(className='description',children = 'Description: Here\'s the body of the thing.'),
                html.Div(children = 'You have X number of tokens left.', style={'color':'orange'}),
            ]
        ),
        html.Div(
            className='three-columns',
            children = [
                html.Div(
                    'Col 1',
                    style = {'width':'30%', 'margin':'0 0 0'}
                ),
                html.Div(
                    'Col 2',
                    style = {'width':'30%', 'margin':'0 0 0'}
                ),
                html.Div(
                    'Col 3',
                    style = {'width':'30%', 'margin':'0 0 0'}
                ),
            ],
        ),
        html.Div(
            className='row',
            children = [
                html.Div(children = 'Something is here.'),
                html.Div(children = 'Something else is here.'),
            ]

        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
