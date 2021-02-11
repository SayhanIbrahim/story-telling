import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

index_page = html.Div([
    dbc.Row([dbc.Col(html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}))]),
    dbc.Row([
            dbc.Col(html.Div(), width=2),
            dbc.Col(html.Div([
                    html.Hr(),
                    html.P("Notre objectif dans ce projet est la visualisation des données"),
                    html.P("Dans ce projet, nous essaierons de visualiser les effets de Covid-19 sur l'économie mondiale."),
                    html.P("Vous pouvez trouver des explications plus détaillées dans le fichier de projet."),
                    html.Hr(),
                    html.Iframe(id="embedded-pdf", src="assets/Data_Storytelling.pdf", width="1200", height="750"),
                    html.Br(),
                    dcc.Link('Go back to home', href='/'),          
                    html.Br(),
            ]), width=8),
            dbc.Col(html.Div(dcc.Link('Go to Next Page ', href='/research'),), style={'textAlign':'center'}, width=2),
        ]),
    ])

research_page = html.Div([
    dbc.Row([dbc.Col(html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}))]),
    dbc.Row([
            dbc.Col(html.Div(dcc.Link('Go to Previous Page ', href='/'),), style={'textAlign':'center'}, width=2),
            dbc.Col(html.Div([
                    html.Hr(),
                    html.P("Un exemple de recherche que j'ai trouvé et aimé lors de mes recherches sur ce sujet sur Internet."),
                    html.Hr(),
                    html.Iframe(id="embedded-pdf", src="assets/research.pdf", width="1200", height="750"),
                    html.Br(),
                    dcc.Link('Go back to home', href='/'),          
                    html.Br(),
            ]), width=8),
            dbc.Col(html.Div(dcc.Link('Go to Next Page ', href='/page-1'),), style={'textAlign':'center'}, width=2),
        ]),
    ])

