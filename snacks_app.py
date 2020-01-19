# Import the dash packages
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_table
from flask import Flask
from flask.logging import logging
import pathlib


# ----------------------------------------------------------------
# Set up the logger
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} | {levelname} | {name} | {message}", style="{"
)
logger = logging.getLogger(__name__)



# ----------------------------------------------------------------
# Set up the styles
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
server = Flask(__name__)

app = dash.Dash(__name__, server=server)
app.config.suppress_callback_exceptions = True

# ---------------------------------------------
# Get the paths
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# ---------------------------------------------



app.layout = html.Div(
    children =[
        html.Div(
            className='header',
            children = [
                dcc.Store(id='tokens-memory', storage_type='session'),
                html.H1(className='headline', children = 'Snacks App'),
                html.Div(className='description', children = 'Description: Here\'s the body of the thing.'),
                html.Div(id='tokens-summary', className='description-emphasis', children = 'You have 10 tokens left.'),
                ]
            ),
        html.Div(
            className='main-body',
            children = [
                html.Div(
                    className='three-columns',
                    children = [
                        html.Div(
                            id='choice-column-1',
                            className='choice-column',
                            children = [
                                html.Div('Col 1'),
                                html.Button(
                                    id='choice-col-1-button',
                                    className='choice-button',
                                    children='Choose Me'
                                )
                            ]
                        ),
                        html.Div(
                            id='choice-column-2',
                            className='choice-column',
                            children = [
                                html.Div('Col 1'),
                                html.Button(
                                    id='choice-col-2-button',
                                    className='choice-button',
                                    children='Choose Me'
                                )
                            ]
                        ),
                        html.Div(
                            id='choice-column-3',
                            className='choice-column',
                            children = [
                                html.Div('Col 1'),
                                html.Button(
                                    id='choice-col-3-button',
                                    className='choice-button',
                                    children='Choose Me'
                                )
                            ]
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
    ]
)


### Load the proper calbacks!
from callbacks import choices
choices.register_callbacks(app)

port = 5000
url = f"http://127.0.0.1:{port}"

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True,port=port)
