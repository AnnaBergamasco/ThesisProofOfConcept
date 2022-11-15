import plotly.graph_objects as go



fig = go.Figure()

fig.add_trace(go.Box(y=[71, 86, 25, 151, 145, 214, 142, 185, 153, 111, 79, 116, 18, 138, 30, 98, 147, 68, 0, 46],
            name="NSGA-III"
            ))

fig.add_trace(go.Box(y=[25, 142, 47, 142, 161, 66, 214, 126, 144, 132, 241, 94, 57, 162, 78, 135, 17, 147, 144, 0], 
            name="U-NSGA-III"
            ))

fig.add_trace(go.Box(y=[0, 2, 0, 5, 18, 0, 7, 115, 235, 1, 437, 28, 7, 2, 0, 3, 20, 6, 18, 441],
            name="AGE-MOEA"
            ))

fig.add_trace(go.Box(y=[8, 8, 6, 53, 12, 13, 26, 12, 4, 47, 20, 35, 38, 3, 17, 27, 6, 8, 1, 32],
            name="C-TAEA"
            ))

fig.add_trace(go.Box(y=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
            name="MOEA-D"
            ))

fig.add_trace(go.Box(y=[1, 1, 2, 2, 1, 4, 2, 1, 0, 1, 2, 0, 2, 1, 0, 1, 2, 3, 2, 2], 
            name="RANDOM"
            ))

fig.update_traces(boxpoints='all', jitter=0)
fig.show()
