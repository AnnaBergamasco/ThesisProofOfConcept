import plotly.express as px
import plotly.graph_objects as go



fig = go.Figure()

fig.add_trace(go.Box(y=[48, 90, 12, 80, 86, 43, 32, 65, 21, 0, 118, 98, 108, 11, 59, 57, 17, 18, 33, 77],
            name="NSGA-III"
            ))

fig.add_trace(go.Box(y=[37, 2, 95, 53, 38, 34, 77, 89, 80, 31, 69, 31, 19, 40, 68, 10, 36, 19, 66, 30], 
            name="U-NSGA-III"
            ))

fig.add_trace(go.Box(y=[178, 178, 188, 168, 175, 162, 204, 212, 162, 188, 0, 180, 96, 181, 202, 180, 197, 133, 191, 128],
            name="AGE-MOEA"
            ))

fig.add_trace(go.Box(y=[106, 100, 97, 62, 100, 42, 104, 80, 14, 42, 92, 0, 137, 118, 117, 112, 127, 117, 115, 123],
            name="C-TAEA"
            ))

fig.add_trace(go.Box(y=[0, 486, 0, 0, 0, 0, 593, 0, 190, 0, 0, 0, 0, 0, 0, 470, 0, 0, 0, 0], 
            name="MOEA-D"
            ))

fig.add_trace(go.Box(y=[1, 0, 1, 0, 2, 1, 1, 2, 0, 0, 1, 1, 0, 0, 1, 0, 2, 0, 0, 2], 
            name="RANDOM"
            ))

fig.update_traces(boxpoints='all', jitter=0)
fig.show()
