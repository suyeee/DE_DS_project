import pandas as pd
import json
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import math


state_geo1 = json.load(open('map (7).zip.geojson', encoding='utf-8'))
df = pd.read_csv('one_day.csv', encoding='utf-8')
df_p = pd.read_csv('one_day_predicted.csv', encoding='utf-8')
df['sigun_code'] = df['sigun_code'].astype(str)

latitude = 35.565
longitude = 127.986

#token = open(".mapbox_token").read()



suburbs = df['stnNm'].str.title().tolist()
suburbs_p = df_p['지점명'].str.title().tolist()

# trace_left = []
# trace_left.append(go.Choroplethmapbox(
#     geojson=state_geo1,
#     locations = df['sigun_code'].tolist(),
#     z=df['ta'].tolist(),
#     text=suburbs,
#     featureidkey='properties.merged',
#     zmin = min(df['ta'].tolist())-0.5,
#     zmax = max(df['ta'].tolist())+0.5,
#     visible=True,
#     subplot='mapbox',
#     colorbar=dict(x=0.7),
#     colorscale='Blackbody',
    
#     hovertemplate="<b>%{text}</b><br><br>" +
#                     "value: %{z}<br>" +
#                     "<extra></extra>"
    
# ))

# trace_right = []
# trace_right.append(go.Bar(
#     x=df.sort_values(['ta'],ascending=False).head(10)['ta'],
#     y=df.sort_values(['ta'],ascending=False).head(10)['stnNm'].str.title().tolist(),
#     xaxis = 'x2',
#     yaxis = 'y2',
#     marker = dict(
#         color='blue',
        
#     ),
#     visible=True,
#     orientation='h',
# ))

layout = go.Layout(
    autosize=True,
    mapbox=dict(
        domain={'x':[0,0.7], 'y':[0,1]},
        center=dict(lat=latitude, lon=longitude),
        style="open-street-map",
        zoom=5
    ),
    xaxis2={
        'domain':[0.77,1],
        'side':'right',
        'anchor':'x2',
    },
    yaxis2={
        'domain':[0,1],
        'anchor':'y2',
        'autorange':'reversed',
    },
    margin=dict(l=80,r=20,t=70,b=70),
    
)
# fig = go.Figure(data=trace_left+trace_right, layout=layout)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#,dbc.themes.BOOTSTRAP

app =Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H1('Interactive dashboard for wildfire prediction and weather info'),
    dcc.Dropdown(['WEATHER','WILDFIRE'], 'WEATHER', id = 'map-dropdown',style={"width": 200}),
    dcc.Graph(id="graph"),
    dcc.Interval(
        id = 'interval-component',
        interval=1*10000,
        n_intervals=0
    ),
    html.Div([
        html.Div([
        html.H6('산불 통계 확인',style=dict(textAlign='center')),
        html.Button(html.A('바로가기',href='https://public.tableau.com/shared/NYJRQC2W2?:display_count=n&:origin=viz_share_link', title='link'),style={'marginBottom':50, 'align':'center'}),
        html.Div(id='container')
        ], style=dict(textAlign='center')),
        html.Div([
            dash_table.DataTable(
                
                data = df_p.to_dict('records'),
                columns=[
                    {'name' : i, 'id' : i, 'deletable': False, "selectable":False} for i in df_p.columns
                ],
                editable=False,
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                row_selectable="multi",
                row_deletable=False,
                selected_rows=[],
                page_action="native",
                page_current=0,
                page_size=6,

                style_cell_conditional=[
                    {
                        'if': {'column_id': c},
                        'textAlign': 'left'
                    } for c in ['Date', 'Region']
                ],
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    }
                ],
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold'
                },
                
            )
        
        ])
    ], className='row')

])

@app.callback(
    Output('graph', 'figure'),
    Input('map-dropdown','value'),
    Input('interval-component','n_intervals')
)
def display_choropleth(map_kind, interval):
    if map_kind=='WEATHER':
        trace_left = []
        trace_left.append(go.Choroplethmapbox(
            geojson=state_geo1,
            locations = df['sigun_code'].tolist(),
            z=df['ta'].tolist(),
            text=suburbs,
            featureidkey='properties.merged',
            zmin = min(df['ta'].tolist())-0.5,
            zmax = max(df['ta'].tolist())+0.5,
            visible=True,
            subplot='mapbox',
            colorbar=dict(x=0.7),
            colorscale='Blues',
            
            hovertemplate="<b>%{text}</b><br><br>" +
                            "value: %{z}<br>" +
                            "<extra></extra>"
            
        ))

        trace_right = []
        trace_right.append(go.Bar(
            x=df.sort_values(['ta'],ascending=False).head(10)['ta'],
            y=df.sort_values(['ta'],ascending=False).head(10)['stnNm'].str.title().tolist(),
            xaxis = 'x2',
            yaxis = 'y2',
            marker = dict(
                color='blue',
                
            ),
            visible=True,
            orientation='h',
        ))
    else:
        trace_left = []
        trace_left.append(go.Choroplethmapbox(
            geojson=state_geo1,
            locations = df_p['sigun_code'].tolist(),
            z=df_p['proba'].map(lambda x:x*100).tolist(),
            text=suburbs_p,
            featureidkey='properties.merged',
            zmin = min(df_p['proba'].map(lambda x:x*100).tolist())-0.5,
            zmax = max(df_p['proba'].map(lambda x:x*100).tolist())+0.5,
            visible=True,
            subplot='mapbox',
            colorbar=dict(x=0.7),
            colorscale='Blues',
            
            hovertemplate="<b>%{text}</b><br><br>" +
                            "value: %{z}<br>" +
                            "<extra></extra>"
            
        ))

        trace_right = []
        trace_right.append(go.Bar(
            x=df_p.sort_values(['proba'],ascending=False).head(10)['proba'],
            y=df_p.sort_values(['proba'],ascending=False).head(10)['지점명'].str.title().tolist(),
            xaxis = 'x2',
            yaxis = 'y2',
            marker = dict(
                color='blue',
                
            ),
            visible=True,
            orientation='h',
        ))
    fig = go.Figure(data=trace_left+trace_right, layout=layout)
    return fig

@app.callback(
    Output('container', 'children'),
    Input('interval-component','n_intervals')
)
def display_proba(mapkind):
    locations = df_p['지점명'].tolist()[:10]
    probas = df_p['proba'].map(lambda x:x*100).tolist()[:10]
    merged = list(zip(df_p['지점명'].tolist(),df_p['proba'].map(lambda x:x*100).tolist()))
    
    return html.Div([
        html.H6('산불 발생 위험 지역 상위 10 지역'),
        html.Div([
            html.Tr([html.Th(i) for i in df_p.sort_values(['proba'],ascending=False).head(10)['지점명'].str.title().tolist()]),
            html.Tr([html.Td(str(round(k*100))+'%') for k in df_p.sort_values(['proba'],ascending=False).head(10)['proba'].tolist()])
        ],style=dict(display='inline-block'))
        
    ],style=dict(textAlign='center'))






app.run_server(debug=True)