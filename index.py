import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from data import df, final_df
import callbacks

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    html.Div([
        html.H1('CO2 Production by cars'),
        html.P('Data Source: Canada 2014')
    ]),
    html.Div([
        html.Div([
            html.Label('Cylinders'),
            html.P('Pick the number of cylinders'),
            dcc.Slider(
                id = 'cylinders',              
                marks={i: '{}'.format(i) for i in range(1,10)},
                min = 1,
                max = 10,
                step = 0.1,
                value = 3,
            ),
        ], className = 'three columns'),
        html.Div([
            html.Label('Engine'),
            html.P('Enter an approx engine size: (eg: 4.5)'),
            dcc.Input(
                id = "engine_size",
                placeholder = 'Enter engine size',
                type = 'number',
                value = 2.4
            ),
        ], className = 'three columns'),
    
        html.Div([
            html.Label('MPG)'),
            html.P('Approx Miles per Gallong(MPG):(eg: 22)'),
            dcc.Input(
                id = "mpg",
                placeholder = 'Enter combined mpg',
                type = 'number',
                value = 21
            ),
        ], className = 'three columns'),
    ], className = 'row'),
    html.Br(),
    html.Div([
        html.Div([
            html.Div(id = "text", style= {'font-size': 24}) ,     
            html.P(id = 'emi', style={'color': 'red', 'font-size': 24}),
        ], className = 'ten columns')
        
    ], className = 'row'),
    
], className = "offset-by-one column row")



if __name__ == '__main__':
    app.run_server(debug=True)
