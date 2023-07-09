import requests
from lxml import etree
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

url = 'https://nba.hupu.com/stats/players'

response = requests.get(url).text
#html = etree.HTML(response)

players = []

for i in range(2,32):
    cur = []
    # 姓名数据解析
    name = etree.HTML(response).xpath("//table[@class='players_table']/tbody/tr[{}]/td[2]/a/text()".format(i))
    # 球队数据解析
    team = etree.HTML(response).xpath("//table[@class='players_table']/tbody/tr[{}]/td[3]/a/text()".format(i))
    # 得分数据解析
    core = etree.HTML(response).xpath("//table[@class='players_table']/tbody/tr[{}]/td[4]/text()".format(i))
    # 得分命中率数据解析
    shooting = etree.HTML(response).xpath("//table[@class='players_table']/tbody/tr[{}]/td[6]/text()".format(i))
    # 三分命中率数据解析
    threeshooting = etree.HTML(response).xpath("//table[@class='players_table']/tbody/tr[{}]/td[8]/text()".format(i))
    # 罚球命中率数据解析
    freeshooting = etree.HTML(response).xpath("//table[@class='players_table']/tbody/tr[{}]/td[10]/text()".format(i))
    cur.append(name[0])
    cur.append(team[0])
    cur.append(core[0])
    cur.append(shooting[0])
    cur.append(threeshooting[0])
    cur.append(freeshooting[0])
    players.append(cur)
print(players)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    # 指定图的id
    dcc.Graph(id = 'graph-with-slider'),
    # 定义滑块的各项属性
    dcc.Slider(
        id = 'class-slider',
        min = 1,
        max = 4,
        value = 2,
        marks = {'1':'得分条形图','2':'命中率条形图','3':'得分折线图','4':'三分命中率散点图'},
        step = None
    )
])
# 定义回调函数，使用‘@app.callback()'参数装饰器来装饰该回调函数，输出绑定图id，输入绑定滑块值
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('class-slider','value')]
)
def update_output_div(input_value):
    # 当滑块滑至1时，即输入值为1，返回得分条形图
    if input_value == 1:
        fig1 = dict(
            data=[{'x': [i+1], 'y': [float(players[i][2])], 'type': 'bar', 'name': '{}'.format(players[i][0])} for i in range(len(players))],
            layout = dict(title = 'NBA2018-2019赛季常规赛得分榜前十各项数据比较')
        )
        return fig1
    # 当滑块滑至3，即输入值为3时，返回球员得分折线图
    if input_value == 3:
        x = []
        y = []
        for player in players:
            x.append(player[0])
            y.append(player[2])
        fig2 = dict(
            data=[
                {'x':x,'y':y,'type':'Scatter','name':'Core'}
            ],
            layout ={
                'title': '球员得分折线图'
            }
        )
        return fig2
    # 当滑块滑至2时，即输入值为2，返回命中率条形图
    if input_value == 2:
        fig3 = dict(
            data=[

                {'x':[players[i][0]],'y':[float(players[i][3][0:2])],'type':'bar','name':'{}'.format(players[i][0])}for i in range(len(players))


            ],
            layout=dict(title='球员命中率条形图')
        )
        return fig3
    # 当滑块滑至4时，即输入值为4，返回得分命中率与三命中率散点图
    if input_value==4:
        x = []
        y = []
        team = []
        for player in players:
            x.append(float(player[3][0:2]))
            if len(player[4])==5:
                y.append(float(player[4][0:3]))
            else:
                y.append(float(player[4][0:2]))
            team.append(player[1])
        fig4=dict(
            data = [
                go.Scatter(
                    x = [x[i]],
                    y = [y[i]],
                    text = team,
                    name = players[i][0],
                    mode='markers',
                    opacity=0.8,
                    marker=dict(size=15, line=dict(width=0.5, color='white'))
                )for i in range(len(players))
            ],
            layout=go.Layout(

                xaxis=dict(type='log', title='得分命中率'),
                yaxis=dict(title='三分命中率', range=[10, 50]),
                margin=dict(l=40, b=40, t=10, r=10),
                hovermode='closest',
                title = '球员得分命中率与三分命中率',
            )
        )

        return fig4

if __name__ == '__main__':
    # 开启服务，指定端口号为7000
    app.run_server(port=7000)



