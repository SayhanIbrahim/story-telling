import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from sklearn import linear_model, tree, neighbors

import pickle


pickle_in1 = open('assets/listPickle','rb')
#unpickling the list and assigning to the list object
countries = pickle.load(pickle_in1) # pickled list of all the countries
models = {'Regression Linear ': linear_model.LinearRegression,
          'Decision Tree ': tree.DecisionTreeRegressor,
          'k-NN ': neighbors.KNeighborsRegressor,}

page_4_layout = html.Div([
    dbc.Row([dbc.Col(html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}))]),
    dbc.Row([dbc.Col(html.Div(dcc.Link('Go to Previous Page ', href='/page-3'),), style={'textAlign':'center'}, width=2),
            dbc.Col(html.Div([html.Hr(),
                    html.P("Sur cette page, vous pouvez voir mon travail sur 3 méthodes différentes qui peuvent être utilisées pour estimer les taux de mortalité de covid-19. (régression linéaire, k-NN, arbre de décission)."),
                    html.P("Comme les conditions de chaque pays (le nombre de cas, le nombre de décès, le niveau de développement humain, la stratégie de confinement) sont différentes, j'ai évalué chaque pays en lui-même afin d'obtenir des résultats plus précis."),
                    html.P("J'ai utilisé l'ensemble de données transformé pour être plus precis."),
                    html.Hr(),          
                              
                    html.P("Select Country:"),
                            dcc.Dropdown(id='dropdown-5', multi=False, className="four columns",
                                    options=[{'label':name, 'value':name} for name in countries],
                                    value = countries[68]),
                    html.P("Select Model:"), 
                            dcc.RadioItems(id='model-name',
                                    options=[{'label': x, 'value': x} 
                                            for x in models],
                                    value='Decision Tree ',
                                    labelStyle={'display': 'block'},),
                            dcc.Graph(id="graph-7"),
                    html.Br(),
                    dcc.Link('Go back to home', href='/'),          
                    html.Br(),
                    
            ]), width=8),
            dbc.Col(html.Div(dcc.Link('Go to Next Page ', href='/page-5'),), style={'textAlign':'center'}, width=2),
        ]),
    ])