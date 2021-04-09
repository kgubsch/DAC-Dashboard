import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv('C:\\Users\\gubsc\\OneDrive\\Documents\\Carbon Visions\\DAC Dashboard\\TEA_Data.csv')
#print(df.dtypes)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
fig = px.scatter(df, x="Cycle Time (min)", y="MAB 100k Cycles ($/kg)",
                 size=pd.to_numeric(df["Full Swing Capacity (mmol/g)"]), color="Sorbent", hover_name="Sorbent",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='capacity-vs-cycle-time',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)