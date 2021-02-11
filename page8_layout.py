import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


continentlist=['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']

page_8_layout = html.Div([
    dbc.Row([dbc.Col(html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}))]),
    dbc.Row([
            dbc.Col(html.Div(dcc.Link('Go to Previous Page ', href='/page-7'),), style={'textAlign':'center'}, width=2),
            dbc.Col(html.Div([
                html.Hr(),
                    html.P("Dans cette page, vous pouves evaluer le nombre de cas et de deces dans chaque continent. J'ai utilisé la méthode du diagramme en barres pour comparer pour chaque pays au sein de chaque continent. J'ai regroupé les pays par continents, car je pensais qu'il n'y aurait pas de graphique significatif lorsque tous les pays seraient reflétés en même temps. Il n'y avait pas de colonne continents dans notre ensemble de données, j'ai donc utilisé «gapmider» pour créer une nouvelle colonne contenant tous les continents de chaque pays."),
                    html.P("Dans le deuxième graphique, le nombre de deces a été utilisé."),
                    html.P("J'ai utilisé l'ensemble de données réel."),
                    html.Hr(),
                dcc.Dropdown(
                                    id='dropdown-7', multi=False, className="four columns",
                                    options=[{'label':name, 'value':name} for name in continentlist],
                                    value = continentlist[1],),
                    html.Hr(),
                    html.P("Select Month :"), 
                    html.Br(),
                           dcc.Slider(
                                id='my-slider-3',
                                min=0,
                                max=10,
                                step=1,
                                value=10,
                            ),
                            html.Div(id='slider-output-container-3'),
                    html.Br(),
                    html.Div([
                    html.Div(dcc.Graph(id='graph-13')),
                    html.Div(dcc.Graph(id='graph-14')),], className="row"),
                    html.Br(),
                    dcc.Link('Go back to home', href='/'),          
                    html.Br(),
            ]), width=8),
            dbc.Col(html.Div(dcc.Link('Go to Next Page ', href='/page-9'),), style={'textAlign':'center'}, width=2),
        ]),
    ])