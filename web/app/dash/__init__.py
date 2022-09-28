import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd


df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)



df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)


app_layout = html.Div([
    dcc.Graph(
        id='index_home',
        figure=fig
    )
])


def init_dash(app):
    dash_app = dash.Dash(server=app, routes_pathname_prefix="/dashapp/")
    dash_app.layout = app_layout
    return dash_app.server
