import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from data import df, final_df


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


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


@app.callback(
    Output ('text', 'children'),
    [Input('engine_size', 'value'),
    Input('mpg', 'value'),
    Input('cylinders', 'value')]
)
def output_div(engine_size,mpg,cylinders):
    if engine_size == None:
        engine_size = 0 
    if mpg == None:
        mpg = 0    
    return f"Cylinder: {cylinders}, Engine-size: {engine_size}, MPG: {mpg}."

@app.callback(
    Output('emi','children'),
    [Input('engine_size', 'value'),
    Input('mpg', 'value'),
    Input('cylinders', 'value')]
)
def co2_emi(engine_size,mpg,cylinders):
    if engine_size == None:
        engine_size = 0 
    if mpg == None:
        mpg = 0 
    pred_co2 = 319.0 + (8.41 * engine_size) + (5.84 * cylinders) + (-4.9 * mpg)
    return f"The total CO2 emission of this vehicle is: {pred_co2}"




if __name__ == '__main__':
    app.run_server(debug=True)

