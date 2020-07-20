import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd


import Prior
import Data
pi = Prior.Prior(name = 'Beta', size = 1000, par = [1, 1], random_state = 1234).Prior_MCsim()
p = Data.Data(name = 'Binomial', pi = pi, cost_fix = 0.5, cost_var = 1, \
    sales_volume = 1, cost_warranty = 0.8, cost_reliability_growth = 10)
#df = p.Optimal_Data(c_list = [0,1,2], R_list = [0.5, 0.6, 0.7], thres_CR = 0.05).head(30)
df = p.All_Data(n_list = [0,1,2,3,4,5,6,7,8,9,10], c_list = [0,1,2], R_list = [0.5, 0.6, 0.7]).head(10)

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


#df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
#available_indicators = df['Indicator Name'].unique()

available_indicators = df.columns.unique()

app.layout = html.Div([
    html.H4(children='BRDT Data'),
    generate_table(df),
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='R'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='CR'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        id='n--slider',
        min=df['n'].min(),
        max=df['n'].max(),
        value=df['n'].max(),
        marks={str(n): str(n) for n in df['n'].unique()},
        step=None
    )
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value'),
     Input('n--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 n_value):
    dff = df[df['n'] == n_value]

    fig = px.scatter(x=dff[xaxis_column_name],
                     y=dff[yaxis_column_name],
                     hover_name=dff[dff['n'] == n_value]['Cost_exp'])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name, 
                     type='linear' if xaxis_type == 'Linear' else 'log') 

    fig.update_yaxes(title=yaxis_column_name, 
                     type='linear' if yaxis_type == 'Linear' else 'log') 

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)