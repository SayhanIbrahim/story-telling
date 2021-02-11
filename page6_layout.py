import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


page_6_layout = html.Div([
    dbc.Row([dbc.Col(html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}))]),
    dbc.Row([
            dbc.Col(html.Div(dcc.Link('Go to Previous Page ', href='/page-5'),), style={'textAlign':'center'}, width=2),
            dbc.Col(html.Div([html.Hr(),
                    html.P("Dans le graphique de cette page, j'ai utilisé l'ensemble de données pour montrer la somme du nombre de cas et de deces mensuels de tous les pays."),
                    html.P("Vous pouvez examiner l'évolution du nombre de cas dans le monde par mois."),
                    html.P("Vous pouvez voir qu'en moins d'un an, Covid-19 infecte plus de 40 millions de personnes dans le monde dont plus d'un million de deces."),
                    html.Hr(),
                html.P("Select Data:"), 
                            dcc.Checklist(id="checklist-5",
                                    options=[   {'label': 'Total Cases', 'value': 'total_cases'},
                                                {'label': 'Total Deaths', 'value': 'total_deaths'},],
                                    value=['total_cases','total_deaths'],
                                    labelStyle={'display': 'block'}),
                    html.Hr(),
                    html.Div([html.Div(dcc.Graph(id='graph-10'), className="four columns"),], className="row"),
                    html.Br(),
                    dcc.Link('Go back to home', href='/'),          
                    html.Br(),
            ]), width=8),
            dbc.Col(html.Div(dcc.Link('Go to Next Page ', href='/page-7'),), style={'textAlign':'center'}, width=2),
        ]),
    ])
