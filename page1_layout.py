import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pickle


pickle_in1 = open('assets/listPickle','rb')
#unpickling the list and assigning to the list object
countries = pickle.load(pickle_in1) # pickled list of all the countries

page_1_layout = html.Div([
    dbc.Row([dbc.Col(html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}))]),
    dbc.Row([
            dbc.Col(html.Div(dcc.Link('Go to Previous Page ', href='/research'),), style={'textAlign':'center'}, width=2),
            dbc.Col(html.Div([
                    html.Hr(),
                    html.P("Sur cette page, vous pouvez comparer le nombre de cas et le nombre de deces et comment ils ont évolué au fil du temps par pays, et vous pouvez avoir une idée des pays qui sont réellement touchés."),
                    html.P("Le premier graphique contient l'évolution du nombre de cas au fil du temps."),
                    html.P("Le deuxième graphique contient l'évolution du nombre de deces au fil du temps."),
                    html.P("Des données réelles ont été utilisées dans ces graphiques."),
                    html.Hr(),
                                
                    dcc.Dropdown(id='dropdown-1', multi=True, className="four columns",
                                    options=[{'label':name, 'value':name} for name in countries],
                                    value = countries[68:69],),
                    html.Hr(),
                    html.Div([
                    html.Div(dcc.Graph(id='graph-1'), className="four columns"),
                    html.Div(dcc.Graph(id='graph-2'), className="four columns"),], className="row"),

                    html.Br(),
                    dcc.Link('Go back to home', href='/'),          
                    html.Br(),
            ]), width=8),
            dbc.Col(html.Div(dcc.Link('Go to Next Page ', href='/page-2'),), style={'textAlign':'center'}, width=2),
        ]),
    ])
