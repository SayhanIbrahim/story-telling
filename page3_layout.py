import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pickle


pickle_in1 = open('assets/listPickle','rb')
#unpickling the list and assigning to the list object
countries = pickle.load(pickle_in1) # pickled list of all the countries

page_3_layout = html.Div([
    dbc.Row([dbc.Col(html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}))]),
    dbc.Row([dbc.Col(html.Div(dcc.Link('Go to Previous Page ', href='/page-2'),), style={'textAlign':'center'}, width=2),
            dbc.Col(html.Div([
                    html.Hr(),
                    html.P("Dans graphique de cette page, vous pouvez examiner comment chaque pays est touché par le COVID 19, comment le nombre de cas et de deces ont changé au fil du temps, sur les données transformées."),
                    html.Hr(),
                            dcc.Dropdown(id='dropdown-3', multi=False, className="four columns",
                                    options=[{'label':name, 'value':name} for name in countries],
                                    value = countries[68]),
                            dcc.Checklist(id="checklist-1",
                                    options=[   {'label': 'Total Cases', 'value': 'TC'},
                                                {'label': 'Total Deaths', 'value': 'TD'},],
                                    value=['TC','TD'],
                                    labelStyle={'display': 'block'}),
                    html.Div([ 
                    html.Div(dcc.Graph(id='graph-5'), className="four columns"),], className="row"),
                    html.Hr(),
                    html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}),
                    html.Hr(),
                    html.P("Dans deuxième graphique, vous pouvez observer comment la quarantaine appliquée par les pays influe sur le nombre de cas et de deces. "),
                    html.Hr(),
                            dcc.Dropdown(id='dropdown-4', multi=False, className="four columns",
                                    options=[{'label':name, 'value':name} for name in countries],
                                    value = countries[68]),
                            dcc.Checklist(id="checklist-2",
                                    options=[   {'label': 'Total Cases', 'value': 'TC'},
                                                {'label': 'Total Deaths', 'value': 'TD'},
                                                {'label': 'Stringency index', 'value': 'STI'},],
                                    value=['STI','TC','TD'],
                                    labelStyle={'display': 'block'}),
                    html.Div([ 
                    html.Div(dcc.Graph(id='graph-6'), className="eleven columns"),], className="row"),

                    html.Br(),
                    dcc.Link('Go back to home', href='/'),          
                    html.Br(),
                                      
            ]), width=8),
            dbc.Col(html.Div(dcc.Link('Go to Next Page ', href='/page-4'),), style={'textAlign':'center'}, width=2),
        ]),
    ])

