# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import timeConverter as tc
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


#load the file data into the graph
df = pd.read_csv('data/DataSample.csv')

x = df.iloc[:,0].tolist()
y = [x*0.0087 for x in df.iloc[:,1].tolist()]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div(children=[
    html.H1(children='Small Family Dataset'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x=x,
                    y=y,
                    fill='tozeroy',
                    fillcolor='light blue',

                )

            ]
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
