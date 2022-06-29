import plotly.express as px
import plotly.graph_objects as go



fig = go.Figure()

fig.add_trace(go.Box(y=[65, 13, 25, 45, 2, 45, 22, 8, 92, 64, 38, 99, 60, 15, 85, 46, 26, 121, 1, 0],
            name="allDistances"
            ))

fig.add_trace(go.Box(y=[0, 483, 0, 0, 0, 496, 465, 0, 0, 415, 0, 0, 0, 0, 0, 0, 0, 0, 437, 479], 
            name="minDistances"
            ))

fig.update_traces(boxpoints='all', jitter=0)
fig.show()
