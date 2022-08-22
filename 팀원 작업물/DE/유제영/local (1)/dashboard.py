import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv('wildfire_his.csv', index_col=0)
data['발생일시'] = pd.to_datetime(data['발생일시'], format = "%Y%m%d%H%M")
data.sort_values("발생일시", inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Graph(
            figure={
                "data":[
                    {
                        "x": data['발생일시'],
                        "y": data['진화소요시간(분)'],
                        "type":"lines",
                    },
                ],
                "layout":{"title":"Title_1"}
            }
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)