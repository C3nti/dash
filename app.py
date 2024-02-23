import pandas as pd
from dash import html, dcc, callback, Output, Input, dash
import plotly.express as px
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
app = dash.Dash(__name__, requests_pathname_prefix='/Dash/')

app = dash.Dash(serve_locally = False)


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == "__main__":
    app.run_server(debug=True)