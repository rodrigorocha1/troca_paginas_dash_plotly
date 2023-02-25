from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc


class APP:
    def __init__(self):
        self.app = Dash(__name__, use_pages=True)
        self.app.layout = self.get_layout()

    def get_layout(self):
        return html.Div(
            [
                html.H1('Multi-page app with Dash Pages'),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4("Title", className="card-title"),
                            html.H6("Card subtitle", className="card-subtitle"),
                            html.P(
                                "Some quick example text to build on the card title and make "
                                "up the bulk of the card's content.",
                                className="card-text",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        dbc.CardLink(
                                            f"{page['name']} - {page['path']}", href=page["relative_path"]
                                        )
                                    )
                                    for page in dash.page_registry.values()
                                ]
                            ),
                        ]
                    ),
                    style={"width": "18rem"},
                ),

                dash.page_container
            ]

        )

    def rodar_servico(self):
        self.app.run_server(debug=True)


a = APP()
server = a.app.server

for page in dash.page_registry.values():
    print(page["relative_path"], page['path'])


if __name__ == '__main__':
    a.rodar_servico()
