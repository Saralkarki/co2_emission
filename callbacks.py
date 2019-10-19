# callbacks

from app import app
from dash.dependencies import Input, Output


@app.callback(
    Output ('text', 'children'),
    [Input('engine_size', 'value'),
    Input('mpg', 'value'),
    Input('cylinders', 'value')]
)
def output_div(engine_size,mpg,cylinders):   
    return f"Cylinder: {cylinders}, Engine-size: {engine_size}, MPG: {mpg}."

@app.callback(
    Output('emi','children'),
    [Input('engine_size', 'value'),
    Input('mpg', 'value'),
    Input('cylinders', 'value')]
)
def co2_emi(engine_size,mpg,cylinders):
    pred_co2 = 319.0 + (8.41 * engine_size) + (5.84 * cylinders) + (-4.9 * mpg)
    return f"The total CO2 emission of this vehicle is:{pred_co2}"

