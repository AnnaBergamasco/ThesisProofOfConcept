import plotly.graph_objects as go

pvalue_map = [[0.20119, 0.00196, 0.00084, 0.00196, 0.00116],
    [1.22756e-08, 8.34116e-08, 3.93771e-08, 1.12609e-06, None],
    [1.32756e-08, 0.00321, 0.00014, None, None],
    [5.80355e-11, 0.60166, None, None, None],
    [1.32756e-08, None, None, None, None]]

fig1 = go.Figure(data=go.Heatmap(
                   z=pvalue_map,
                   x=['RANDOM', 'NSGA-3', 'U-NSGA-3', 'C-TAEA', 'AGE-MOEA'],
                   y=['MOEA-D', 'AGE-MOEA', 'C-TAEA', 'U-NSGA-3', 'NSGA-3'],
                   hoverongaps = False,
                   colorscale='Reds',
                   text= pvalue_map,
                   texttemplate="%{text}",
                   textfont={"size":20}))
fig1.show()

effect_size_map = [[0.62, 0.78, 0.8, 0.7925, 0.78, None], 
    [0.03875, 0.21325, 0.16125, 0.91375, None, 0.22],
    [0.03875, 0.05625, 0.05, None, 0.08625, 0.2075],
    [0.005, 0.55, None, 0.95, 0.83875, 0.2],
    [0.03875, None, 0.45, 0.94375, 0.76875, 0.22],
    [None, 0.96125, 0.995, 0.96125, 0.96125, 0.38]]

fig2 = go.Figure(data=go.Heatmap(
                   z=effect_size_map,
                   x=['RANDOM', 'NSGA-3', 'U-NSGA-3', 'AGE-MOEA', 'C-TAEA', 'MOEA-D'],
                   y=['MOEA-D', 'C-TAEA', 'AGE-MOEA', 'U-NSGA-3', 'NSGA-3', 'RANDOM'],
                   hoverongaps = False,
                   colorscale='Reds',
                   text=effect_size_map,
                   texttemplate="%{text}",
                   textfont={"size":20}))

fig2.show()