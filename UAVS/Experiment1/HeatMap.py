import plotly.graph_objects as go

pvalue_map = [[1.45089e-11, 2.90178e-11, 1.45089e-11, 1.45089e-11, 1.45089e-11],
    [1.45089e-11, 2.03124e-10, 2.90178e-11, 0.00037, None],
    [1.45089e-11, 6.05601e-08, 3.93771e-08, None, None],
    [1.45089e-11, 0.23535, None, None, None],
    [2.90178e-11, None, None, None, None]]

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

effect_size_map = [[1.0, 1.0, 1.0, 1.0, 1.0, None], 
    [0.0, 0.05, 0.05, 0.1825, None, 0.0],
    [0.0, 0.00789, 0.0025, None, 0.8175, 0.0],
    [0.0, 0.61316, None, 0.9975, 0.95, 0.0],
    [0.0, None, 0.38684,  0.9921, 0.95, 0.0],
    [None, 1.0, 1.0, 1.0, 1.0, 0.0]]

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