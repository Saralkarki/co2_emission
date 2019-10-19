import dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = app.server
app.config.suppress_callback_exceptions = True


app.title("CO2 Emissions Prediction")

# app.config.suppress_callback_exceptions = True