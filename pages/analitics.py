import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)


class Analitics:

    def __init__(self):
        self.layout = self._get_layout()
        self._calbacks()

    def _get_layout(self):
        return html.Div(
            children=[
                html.H1(
                    children='Analitics page'
                ),
                html.Div(
                    [
                        'Select a city',
                        dcc.RadioItems(
                            [
                                'New York City',
                                'Montreal',
                                'San Francisco'
                            ],
                            'Montreal',
                            id='analytics-input'
                        )
                    ]
                ),
                html.Br(),
                html.Div(id='analytics-output'),
            ]
        )

    def _calbacks(self):
        @callback(
            Output(component_id='analytics-output', component_property='children'),
            Input(component_id='analytics-input', component_property='value'))
        def update_city_selected(input_value):
            return f'You selected: {input_value}'


a = Analitics()
layout = a.layout
