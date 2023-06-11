import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Checklist(
        options=['Python语言', 'Julia语言', 'R语言'],
        value=['Python语言', 'R语言']
    ),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization测试中'
            }

        }
    ),
    dcc.Graph(
        id ="graphExample", # ID of graph
        figure ={ # Creating Graph figure
            'data':[
                {'x':[1, 3, 5, 7, 9, 11, 13],
                 'y':[7, 6, 8, 4, 5, 9, 3],
                 'type':'line',
                 'name':'Trucks'},
                {'x':[1, 3, 5, 7, 9, 11, 13],
                 'y':[6, 5, 7, 3, 4, 8, 2],
                 'type':'bar',
                 'name':'Ships'}
            ],
            'layout':{ # Layout of the graph
                'title':'A Basic Graph for Dashboard' # Title of the graph
            }
        }
    ),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization测试中'
            }

        }
    ),
    dcc.Checklist(
        options=[
            {'label': 'Python语言', 'value': '1'},
            {'label': 'Julia语言', 'value': '2'},
            {'label': 'R语言', 'value': '3'},
        ],
        value=['1', '3']
    ),
    dcc.Checklist(
        options={
            '1': 'Python语言',
            '2': 'Julia语言',
            '3': 'R语言',
        },
        value=['2', '3']
    ),
    dcc.Checklist(
        options=[
            {
                'label': html.Img(src=app.get_asset_url('img/python_50px_icon.png')),
                'value': 'Python语言',
            },
            {
                'label': html.Img(src=app.get_asset_url('img/julia_50px_icon.png')),
                'value': 'Julia语言',
            },
            {
                'label': html.Img(src=app.get_asset_url('img/r_50px_icon.png')),
                'value': 'R语言',
            },
        ],
        value=['Python语言', 'R语言']
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)