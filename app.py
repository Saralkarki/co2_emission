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
app.title = 'CO-2 emission by vehicles'
app.layout = html.Div([
    html.Div([
        html.H2('Predicted CO-2 Emission by cars'),
        html.A('Data Source: Original Fuel Consumption Ratings 2000-2014', href = 'https://lnkd.in/eiXxgvw',
        style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold',
        'text-decoration': 'none'}, target = '_blank'),
        html.Br(),
        html.A('Predicting the CO2 emission - Multiple Linear Regression model paper (PDF)', 
        href = 'https://github.com/Saralkarki/statistical_papers/blob/master/Predicting%20CO2%20emission%20using%20multiple%20regression%20model.pdf',
        style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold',
        'text-decoration': 'none'}, target = '_blank'),
    ]),
    html.Br(),
    html.Div([
        html.P('''The dashboard uses multiple linear regression model to predict the CO2 emission. The independent
        variable used to predict the the dependent variable (CO2 emission) are:
                    '''),
    html.Li('Engine Size'),
        html.P(''),
    html.Li('Cylinders'),
    html.Li('Milege Per Gallon(MPG)'),
    ], className = 'twelve columns row', style={'marginBottom': 30}
    ),
    html.Div([
        html.H6('Pick number of cylinders, Engine Size and MPG, and check the CO-2 predicted EMITTED by your vehicle')
    ]),
    html.Div([
        html.Div([
            html.Label('Cylinders', style = {'font-family': 'Helvetica', 'font-weight':'bold'}),
            html.P('Pick the number of cylinders', style = {'font-family': 'Helvetica', 'font-weight':'bold'}),
            html.Div([
                dcc.Slider(
                id = 'cylinders',              
                marks={i: f'{i}' for i in range(1,17)},
                min = 1,
                max = 16,
                step = 1,
                value = 3,
                updatemode='drag'
                ),
            ], className = 'ten columns'),           
        ], className = 'four columns', style = {'background': '#eaf9db','height': 90}),
        html.Div([
            html.Label('Engine', style = {'font-family': 'Helvetica', 'font-weight':'bold'}),
            html.P('Enter an approx engine size: (eg: 4.5)', style = {'font-family': 'Helvetica', 'font-weight':'bold'}),
            dcc.Input(
                id = "engine_size",
                placeholder = 'Enter engine size',
                type = 'number',
                value = 2.4
            ),
        ], className = 'three columns', style = {'background': '#eaf9db'}),
    
        html.Div([
            html.Label('MPG', style = {'font-family': 'Helvetica', 'font-weight':'bold'}),
            html.P('Approx Miles per Gallon(MPG):(eg: 22)', style = {'font-family': 'Helvetica', 'font-weight':'bold'}),
            dcc.Input(
                id = "mpg",
                placeholder = 'Enter combined mpg',
                type = 'number',
                value = 21
            ),
        ], className = 'three columns',style = {'background': '#eaf9db'}),
    ], className = 'row' ),
    html.Br(),
    html.Div([
        html.H5('''The CO2 emitted value changes according to the multiple linear regression model 
            as the input changes''', style={'color': 'black','font-weight': 'bold'}),
        html.Div([           
            html.Div(id = "text", style= {'font-size': 24}) ,     
            html.P(id = 'emi', style = {'font-size': 24,'font-family': 'Helvetica', 'font-weight':'bold', 'color': 'black'}),
        ], className = 'ten columns', style = {"background": '#eaf9db'})
        
    ], className = 'row'),
    html.Div([
        html.P('''
            In general, the lower this figure, the less fuel that a vehicle uses: a car with 90g/km CO2, 
            should have good fuel economy. One with 180g/km CO2 or more will use a lot of fuel.
        '''),
    ]),
    html.Br(),
    html.Br(),
    html.Div([
        html.H1('Regression Model'),
        html.P('''
                The above generated values uses the model as shown in the Regplot to determine the value 
                for predicted CO-2.'''),
        html.P('''Also, the Distplot shows how the predicted values might differ from the target value after 
                applying the regression model.
                '''),       
        html.Img(src = '/static/model_diagram.png')
    ]),
    
], className = "offset-by-one columns row" )


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
    return f"The total CO-2 emission of this vehicle is: {round(pred_co2) } g/km - rounded value"




if __name__ == '__main__':
    app.run_server(debug=True)

