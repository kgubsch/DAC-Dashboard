import dash
import dash_html_components as html
import pandas as pd

df = pd.read_csv('C:\\Users\\gubsc\\OneDrive\\Documents\\Carbon Visions\\DAC Dashboard\\TEA_Data.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='Sorbents from 2019 TEA'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)