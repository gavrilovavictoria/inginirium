import plotly
import plotly.graph_objs as go

import numpy as np

x = np.arange(0, 10, 0.1)

def f1(x):
    return x * (6 - x)


def f2(x):
    return np.sin(x)


fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=f1(x), mode='markers', name='f1(x)= x(6 - x)',
                         marker=dict(color=f1(x), colorscale='Magenta')))

fig.add_trace(go.Scatter(x=x, y=f2(x), mode='lines+markers', name='f2(x) = sin(x)',
                         marker=dict(color=f2(x), colorbar=dict(title="f2(x) = sin(x)"), colorscale='Inferno',
                                     size=50 * abs(f2(x)))))
fig.update_layout(legend_orientation="h",
                  legend=dict(x=.5, xanchor="center"),
                  hovermode="x",
                  margin=dict(l=0, r=0, t=0, b=0))
fig.update_traces(hoverinfo="all", hovertemplate="X: %{x}<br>Y: %{y}")
fig.show()
go.Scatter(x=x, y=f1(x))
