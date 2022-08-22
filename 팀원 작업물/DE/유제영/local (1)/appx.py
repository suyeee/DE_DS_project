import pandas as pd
import json
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.express as px

state_geo1 = json.load(open('map (7).zip.geojson', encoding='utf-8'))
df = pd.read_csv('one_day.csv', encoding='utf-8')
df['sigun_code'] = df['sigun_code'].astype(str)

# for idx, sigun_dict in enumerate(state_geo1['features']):
#     sigun_id = df.loc[(df.지점명 == sigun_dict['properties']['SIG_KOR_NM'][:2]), '지점명'].iloc[0]
    
suburbs = df['sigun_nm'].str.title().tolist()
color_deep = [[0.0, 'rgb(253, 253, 204)'],
              [0.1, 'rgb(201, 235, 177)'],
              [0.2, 'rgb(145, 216, 163)'],
              [0.3, 'rgb(102, 194, 163)'],
              [0.4, 'rgb(81, 168, 162)'],
              [0.5, 'rgb(72, 141, 157)'],
              [0.6, 'rgb(64, 117, 152)'],
              [0.7, 'rgb(61, 90, 146)'],
              [0.8, 'rgb(65, 64, 123)'],
              [0.9, 'rgb(55, 44, 80)'],
              [1.0, 'rgb(39, 26, 44)']]

# trace1 = []
# trace1.append(go.Choroplethmapbox(
#     geojson=state_geo1,
#     locations = df['sigun_code'].tolist(),
#     z=df['소멸위험지수'].tolist(),
#     text = suburbs,
#     featureidkey = "properties.merged",
#     colorscale=color_deep,
#     colorbar=dict(thickness=20, ticklen=3),
#     zmin=0,
#     zmax=df['소멸위험지수'].max() + 0.5,
    
#     visible=False,
#     subplot='mapbox1',
#     hovertemplate="<b>%{text}</b><br><br>" +
#                     "value: %{z}<br>" +
#                     "<extra></extra>"
    
# ))
# trace1[0]['visible'] = True

latitude = 35.565
longitude = 127.986

# layout = go.Layout(
#     title={'text': 'Number of people in Korea / Local extinction in 2018',
#            'font': {'size': 28,
#                     'family': 'Arial'}},
#     autosize=True,

#     mapbox1=dict(
#         domain={'x': [0.3, 1], 'y': [0, 1]},
#         center=dict(lat=latitude, lon=longitude),
#         style="open-street-map",
#         #accesstoken = mapbox_accesstoken,
#         zoom=5),

#     xaxis2={
#         'zeroline': False,
#         "showline": False,
#         "showticklabels": True,
#         'showgrid': True,
#         'domain': [0, 0.25],
#         'side': 'left',
#         'anchor': 'x2',
#     },
#     yaxis2={
#         'domain': [0.4, 0.9],
#         'anchor': 'y2',
#         'autorange': 'reversed',
#     },
#     margin=dict(l=100, r=20, t=70, b=70),
#     paper_bgcolor='rgb(204, 204, 204)',
#     plot_bgcolor='rgb(204, 204, 204)',
# )
#token = open(".mapbox_token").read()
token = open(".mapbox_token").read()

app = Dash(__name__)





app.layout = html.Div([
    html.H4('Interactive dashboard for wildfire prediction and weather info'),
    dcc.Dropdown(['WEATHER','WILDFIRE'], 'WEATHER', id = 'map-dropdown',style={"width": 200}),
    dcc.Graph(id="graph"),
])



@app.callback(
    Output('graph', 'figure'),
    Input('map-dropdown','value')
)
def display_choropleth(map_kind):
    fig = px.choropleth_mapbox(
        df, geojson=state_geo1, color='ta',
        hover_name=df['stnNm'],hover_data=['tm','ta'],
        locations="sigun_code", featureidkey="properties.merged",
        center={"lat": latitude, "lon": longitude}, zoom=6,
        range_color=[min(df['ta'].tolist())-0.5, max(df['ta'].tolist())+0.5])
    fig.update_layout(
        margin={"r":0,"t":60,"l":0,"b":0},
        mapbox_accesstoken=token
    )
    return fig
# @app.callback(
#     Output("graph", "figure"), 
#     Input("candidate", "value"))
# def display_choropleth(candidate):
#     #df = px.data.election() # replace with your own data source
#     #geojson = px.data.election_geojson()
    
#     fig = px.choropleth_mapbox(
#         df, geojson=state_geo1, color='ws',
#         locations="sigun_code", featureidkey="properties.merged",
#         center={"lat": latitude, "lon": longitude}, zoom=6,
#         range_color=[0, max(df['ws'].tolist())+0.5])
#     fig.update_layout(
#         margin={"r":0,"t":0,"l":0,"b":0},
#         mapbox_accesstoken=token
#         )

#     return fig



# fig = px.choropleth_mapbox(df, geojson=state_geo1, locations='sigun_code', color='소멸위험지수',
#                            color_continuous_scale="Viridis",
#                            range_color=[0, 3],
#                            featureidkey='properties.merged',
#                            mapbox_style="carto-positron",
#                            zoom=3, center = {"lat": latitude, "lon": longitude},
#                            opacity=0.5,
#                            labels={'소멸위험지수':'unemployment rate'}
#                           )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
#                   mapbox_accesstoken=token)
# #fig = go.Figure(data=trace1, layout=layout)

# external_stylesheets= ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
# server = app.server

# app.layout = html.Div([
#     html.Div(children=[
#         dcc.Graph(
#             id='example-graph-1',
#             figure=fig
#         )
#     ])
# ])

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.graph_objects as go

# app = dash.Dash(__name__)


# app.layout = html.Div([
#     html.H4('Interactive color selection with simple Dash example'),
#     html.P("Select color:"),
#     dcc.Dropdown(
        
#         options=[
#             {'label': "Gold" , "value":"Gold"},
#             {'label': "MediumTurquoise", "value" : "MediumTurquoise"},
#             {'label': "LightGreen", "value" : "LightGreen"}
#             ],
#         value='Gold',
#         clearable=False,
#         id="dropdown",
        
#     ),
#     dcc.Graph(id="graph"),
# ])


# @app.callback(
#     Output("graph", "figure"), 
#     Input("dropdown", "value"))
# def display_color(color):
#     fig = go.Figure(
#         data=go.Bar(y=[2, 3, 1], # replace with your own data source
#                     marker_color=color))
#     return fig


app.run_server(debug=True)
