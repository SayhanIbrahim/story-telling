import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


page_5_layout = html.Div([
    dbc.Row([dbc.Col(html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}))]),
    dbc.Row([dbc.Col(html.Div(dcc.Link('Go to Previous Page ', href='/page-4'),), style={'textAlign':'center'}, width=2),
            dbc.Col(html.Div([html.Hr(),
                    html.P("Dans le graphique de cette page, vous pouvez observer comment Covid-19 affecte le monde et comment il évolue au fil des mois sur la carte du monde."),
                    html.P("Le premier graphique est basé sur le nombre de cas."),
                    html.P("J'ai utilisé l'ensemble de données transformé pour être plus precis."),
                    html.Hr(),
                    html.P("Select Month:"), 
                    html.Br(),
                           dcc.Slider(
                                id='my-slider',
                                min=0,
                                max=10,
                                step=1,
                                value=0,
                            ),
                            html.Div(id='slider-output-container'),
                    html.Br(),
                            dcc.Graph(id="graph-8"),
                    html.Br(),
                    html.Hr(),
                    html.P("Dans le deuxième graphique, pour le nombre de deces."),
                    html.P("J'ai utilisé l'ensemble de données transformé pour être plus precis."),
                    html.Hr(),
                    html.P("Select Month :"), 
                    html.Br(),
                           dcc.Slider(
                                id='my-slider-1',
                                min=0,
                                max=10,
                                step=1,
                                value=0,
                            ),
                            html.Div(id='slider-output-container-1'),
                    html.Br(),
                            dcc.Graph(id="graph-9"),
                    html.Br(),
                    dcc.Link('Go back to home', href='/'),          
                    html.Br(),
                    
            ]), width=8),
            dbc.Col(html.Div(dcc.Link('Go to Next Page ', href='/page-6'),), style={'textAlign':'center'}, width=2),
        ]),
    ])