
# Import the dash packages
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from flask.logging import logging
import pathlib




# Set up the logger
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} | {levelname} | {name} | {message}", style="{"
)
logger = logging.getLogger(__name__)


def register_callbacks(app):

    @app.callback(
        Output('tokens-memory', 'memory'),

        [
            Input(f'choice-col-1-button', 'n_clicks'),
            Input(f'choice-col-2-button', 'n_clicks'),
            Input(f'choice-col-3-button', 'n_clicks'),
        ],

        [State('tokens-memory', 'memory')]
        )
    def update_tab_1_progress(choice_1, choice_2, choice_3, data):
        """
        Stores what's what on the page.
        """

        if not data:
            data = {'Tokens':10, 'State':{}}
        else:
            data['Tokens'] -=1

        all_choices = [choice_1,choice_2,choice_3]
        for i, choice in enumerate(all_choices):
            data['State'][i] = choice

        # logger.info(f'Updating page progress. Data = {data}')
        return data


    @app.callback(
        Output('tokens-summary', 'children'),
        [Input('tokens-memory', 'memory')]
        )
    def update_tab_1_progress(data):
        """
        Stores what's what on the page.
        """
        if not data:
            raise PreventUpdate
        n = data.get('Tokens')
        output_string = f'You have {n} tokens left'
        logger.info(output_string)

        return output_string

    @app.callback(
        [
            Output(f'choice-col-1-button', 'disabled'),
            Output(f'choice-col-2-button', 'disabled'),
            Output(f'choice-col-3-button', 'disabled'),
            Output(f'tokens-summary', 'style')
        ],
        [Input('tokens-memory', 'memory')],
        [State(f'tokens-summary', 'style')]
        )
    def update_tab_1_progress(data, style):
        """
        Stores what's what on the page.
        """
        if not data:
            raise PreventUpdate
        if not style:
            style = {}

        n = data.get('Tokens')

        if n>0:
            status = False

        if n<=3:
            style['color'] = 'darkred'
        if n<1:
            status = True
            style['font-weight'] = 'bold'
            logger.info('All tokens used. Disabling buttons.')

        return status,status,status, style
