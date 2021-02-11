import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

continentlist=['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']

page_10_layout = html.Div([
    dbc.Row([dbc.Col(html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}))]),
    dbc.Row([
            dbc.Col(html.Div(dcc.Link('Go to Previous Page ', href='/page-9'),), style={'textAlign':'center'}, width=2),
            dbc.Col(html.Div([
                    html.Hr(),
                    html.P("Et passons aux camemberts, vous pouvez imaginer qu'il sera très difficile de déguster un gâteau divisé en plus de 200 tranches. Au lieu de cela, j'ai décidé d'utiliser mon ensemble de données, dont j'avais déjà ajouté les continents, car je trouvais le diagramme à secteurs divisé par continents plus significatif."),
                    html.P("J'ai utilisé le nombre de cas dans le premier graphique et le nombre de deces dans le deuxième graphique."),
                    html.Hr(),
                    html.P("Just some Dilbert comics featuring pie charts. OOOH!"),
                    html.Hr(),
                dcc.Dropdown(
                                    id='dropdown-9', multi=False, className="four columns",
                                    options=[{'label':name, 'value':name} for name in continentlist],
                                    value = continentlist[1],),
                    html.Hr(),
                    html.P("Select Month :"), 
                    html.Br(),
                           dcc.Slider(
                                id='my-slider-5',
                                min=0,
                                max=10,
                                step=1,
                                value=10,
                            ),
                            html.Div(id='slider-output-container-5'),
                    html.Br(),
                    html.Div([

                    html.Div(dcc.Graph(id='graph-17')),
                    html.Div(dcc.Graph(id='graph-18')),], className="row"),
                    html.Br(),
                    dcc.Link('Go back to home', href='/'),          
                    html.Br(),
            ]), width=8),
            dbc.Col(html.Div(), width=2),
        ]),
    ])

