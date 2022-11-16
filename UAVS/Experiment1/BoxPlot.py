import plotly.graph_objects as go



fig = go.Figure()

fig.add_trace(go.Box(y=[776, 652, 627, 481, 639, 658, 542, 841, 494, 887, 664, 774, 603, 571, 555, 665, 888, 575, 732],
            name="NSGA-III"
            ))

fig.add_trace(go.Box(y=[653, 617, 393, 467, 754, 647, 342, 529, 491, 658, 695, 401, 845, 646, 639, 642, 537, 616, 742, 755], 
            name="U-NSGA-III"
            ))

fig.add_trace(go.Box(y=[1304, 968, 1156, 1242, 1243, 1104, 817, 1153, 1246, 1410, 1438, 1295, 1070, 1336, 1016, 1199, 940, 1373, 1256, 1089],
            name="AGE-MOEA"
            ))

fig.add_trace(go.Box(y=[1649, 1461, 1296, 1567, 1230, 1404, 1744, 1660, 1315, 288, 1239, 1348, 1688, 1488, 1165, 1249, 1913, 1795, 1651, 1416],
            name="C-TAEA"
            ))

fig.add_trace(go.Box(y=[3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
            name="MOEA-D"
            ))

fig.add_trace(go.Box(y=[9, 8, 5, 6, 6, 8, 5, 4, 7, 9, 10, 7, 9, 6, 6, 7, 6, 6, 10, 8], 
            name="RANDOM"
            ))

fig.update_traces(boxpoints='all', jitter=0)
fig.show()
