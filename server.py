from dash import Dash, dcc, html, Input, Output, callback, dash_table
import plotly
import plotly.express as px
import csv
import pandas as pd

# apparently plotly docs show this stylsheet...
app = Dash(name = "Yet another Arcade review tracker", external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])

server = app.server

app.layout = [
    html.H1(children='Yet another Arcade review graph', style={'textAlign':'center'}),
    html.Div(children='I love speedrunning figuring out frameworks.'),
    dcc.Interval(
        id='interval-component',
        interval=5*1000, # in milliseconds
        n_intervals=0
    ),
    dcc.Graph(id='pending-graph-content'),
    dcc.Graph(id='reviewed-graph-content'),
    dcc.Graph(id='merged-graph-content'),
    html.H2(children='Raw data', style={'textAlign':'center'}),
    dash_table.DataTable(id="datatable",page_size=25)
]

cached = []
def get_arcade_reviewing_data():
    global cached
    try:
        cached = pd.read_csv('data.csv', header = None, names = [
            "Time",
            "Formatted Time",
            "Hours Approved",
            "Hours Pending"
        ])
        print(cached)
        return cached
    except Exception as ex:
        print("Error syncing arcade data from bg task", ex)
        print("Falling back to cache")
        return cached

@callback(
    Output('pending-graph-content', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n_intervals):
    return px.line(get_arcade_reviewing_data(), x = "Formatted Time", y = "Hours Pending")

@callback(
    Output('reviewed-graph-content', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n_intervals):
    return px.line(get_arcade_reviewing_data(), x = "Formatted Time", y = "Hours Approved")

@callback(
    Output('merged-graph-content', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n_intervals):
    return px.line(get_arcade_reviewing_data(), x = "Formatted Time", y = ["Hours Pending", "Hours Approved"])

@callback(
    Output('datatable', 'data'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n_intervals):
    return get_arcade_reviewing_data().to_dict('records')
    
if __name__ == '__main__':
    app.run(debug=True)