import dash_bootstrap_components as dbc
from dash import dcc, html
from config import COUNTRIES, DEFAULT_KEYWORDS, DEFAULT_START_DATE, DEFAULT_END_DATE

def create_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Google Trends Analysis Dashboard", 
                       className="text-center mb-4 mt-3"),
            ])
        ]),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Search Parameters", className="card-title"),
                        dbc.Form([
                            dbc.Row([
                                dbc.Col([
                                    dbc.Label("Keywords (comma separated)"),
                                    dbc.Input(
                                        id='keyword-input',
                                        value=DEFAULT_KEYWORDS,
                                        type='text',
                                        placeholder="Enter keywords..."
                                    )
                                ], width=12, className="mb-3"),
                            ]),
                            
                            dbc.Row([
                                dbc.Col([
                                    dbc.Label("Start Date"),
                                    dbc.Input(
                                        id='start-date',
                                        value=DEFAULT_START_DATE,
                                        type='date'
                                    )
                                ], width=6),
                                
                                dbc.Col([
                                    dbc.Label("End Date"),
                                    dbc.Input(
                                        id='end-date',
                                        value=DEFAULT_END_DATE,
                                        type='date'
                                    )
                                ], width=6),
                            ], className="mb-3"),
                            
                            dbc.Row([
                                dbc.Col([
                                    dbc.Label("Region"),
                                    dcc.Dropdown(
                                        id='country-dropdown',
                                        options=COUNTRIES,
                                        value='US',
                                        clearable=False
                                    )
                                ])
                            ], className="mb-3"),
                        ])
                    ])
                ], className="mb-4")
            ], width=12)
        ]),
        
        dbc.Row([
            dbc.Col([
                dbc.Spinner(
                    dcc.Graph(
                        id='trends-graph',
                        config={'displayModeBar': True},
                        style={'height': '70vh'}
                    ),
                    color="primary",
                    type="border",
                    fullscreen=False,
                )
            ])
        ]),
        
        dbc.Row([
            dbc.Col([
                html.Div(
                    id='status',
                    className="alert alert-info mt-3",
                    style={'display': 'none'}
                )
            ])
        ]),
        
    ], fluid=True, className="px-4")