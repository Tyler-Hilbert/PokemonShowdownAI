# Plots tree of predicted game state
# Reference - https://plotly.com/python/tree-plots/

import igraph
from igraph import Graph, EdgeSeq
import plotly.graph_objects as go

def make_annotations(pos, text, font_size=25, font_color='rgb(10,10,10)'):
    L=len(pos)
    if len(text)!=L:
        raise ValueError('The lists pos and text must have the same len')
    annotations = []
    for k in range(L):
        annotations.append(
            dict(
                text=text[k], # or replace labels with a different list for the text within the circle
                x=pos[k][0], y=pos[k][1],
                xref='x1', yref='y1',
                font=dict(color=font_color, size=font_size),
                showarrow=False)
        )
    return annotations

XnNames = ['umbreon', 'vaporeon', 'espeon', 'leafeon', 'jolteon', 'umbreon', 'flareon', 'umbreon', 'espeon', 'espeon', 'leafeon', 'vaporeon', 'espeon', 'flareon', 'umbreon']
Xn =      [0,          1,         1,        2,         3,          3,        3,         3,         3,        4,        5,         5,          5,         6,         7]
Yn =      [2,          1,         3,        2,         0,          1,        3,         4,         5,        2,        1,         3,          4,         2,         3]
Xe = [1,  0,  None, 1,  2,  None, 2,  1,  None, 3,  1, None, 3,  3, None,  2,  3, None,  3,  3, None, 3,  3,  None, 3,  5, None, 5,  4,  None, 5,  6,  None, 6,  5,  None, 5,  5,  None, 6,  7,  None]
Ye = [-1, -2, None, -1, -2, None, -2, -3, None, 0, -1, None, 0, -1, None, -2, -3, None, -3, -4, None, -4, -5, None, 0, -1, None, -1, -2, None, -1, -2, None, -2, -3, None, -3, -4, None, -2, -3, None]
Yn = [element * -1 for element in Yn]

position = {}
for k in range(len(Xn)):
    position[k] = [Xn[k], Yn[k]]
L = len(position)

fig = go.Figure()
fig.add_trace(go.Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line=dict(color='rgb(210,210,210)', width=1),
                   hoverinfo='none'
                   ))
fig.add_trace(go.Scatter(x=Xn,
                  y=Yn,
                  mode='markers',
                  name='bla',
                  marker=dict(symbol='circle-dot',
                                size=18,
                                color='#6175c1',    #'#DB4551',
                                line=dict(color='rgb(250,250,250)', width=1)
                                ),
                  text=XnNames,
                  hoverinfo='x',
                  opacity=0.8
                  ))


axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            )

fig.update_layout(title= 'Hardcoded Game State',
              annotations=make_annotations(position, XnNames),
              font_size=12,
              showlegend=False,
              xaxis=axis,
              yaxis=axis,
              margin=dict(l=40, r=40, b=85, t=100),
              hovermode='closest',
              plot_bgcolor='rgb(248,248,248)'
              )
fig.show()
