
from copy import copy
import plotly.graph_objects as go

categories = ['S0 e1 S1','S0 e1 S2', 'S0 e1 S6', 'S3 e1 S1', 'S3 e1 S4', 'S3 e1 S5']

fig1 = go.Figure()

fig1.add_trace(go.Scatterpolar(
    r = [0.007598670378823384, -0.005475649037884112, 0.003046069529013114, 9.99999999999994e-05, 0.0, 9.999999999998899e-05],
    theta = categories,
    fill = 'toself',
    name = 'min RANDOM'
))

fig1.add_trace(go.Scatterpolar(
    r = [0.007583341070633805, -0.008018893859577103, 0.002844446101142129, 9.99999999999994e-05, 0.0, 9.999999999998899e-05],
    theta = categories,
    fill = 'toself',
    name = 'min NSGA-III'
))

fig1.add_trace(go.Scatterpolar(
    r = [0.007583450823347492, -0.008536780363509577, 0.0028457821000263993, 9.99999999999994e-05, 0.0, 9.999999999998899e-05],
    theta = categories,
    fill = 'toself',
    name = 'min U-NSGA-III'
))

fig1.add_trace(go.Scatterpolar(
    r = [0.007583365616792707, -0.008974595093018678, 0.002834976383143386, 9.99999999999994e-05, 0.0, 9.999999999998899e-05],
    theta = categories,
    fill = 'toself',
    name = 'min C-TAEA'
))

fig1.add_trace(go.Scatterpolar(
    r = [0.007583333726698659, -0.009112849124759625, 0.002831590069578596, 9.99999999999994e-05, 0.0, 9.999999999998899e-05],
    theta = categories,
    fill = 'toself',
    name = 'min AGE-MOEA'
))

fig1.update_layout(
    polar = dict (radialaxis = dict(
        visible = True,
        range = [0.02, -0.01]
    )),
    showlegend = True
)

fig1.show()

fig2 = go.Figure()

fig2.add_trace(go.Scatterpolar(
    r = [0.012901185107996272, 0.019315010413081438, 0.00900041262478597, 0.003779911111111111, 0.0012781444444444443, 0.005058055555555566],
    theta = categories,
    fill = 'toself',
    name = 'avg RANDOM'
))

fig2.add_trace(go.Scatterpolar(
    r = [0.012067100446369862, 0.014719300232457709, 0.012253217085680003, 0.0028643055555555557, 0.000846461111111111, 0.003710766666666673],
    theta = categories,
    fill = 'toself',
    name = 'avg NSGA-III'
))

fig2.add_trace(go.Scatterpolar(
    r = [0.012153637068077055, 0.014185063778808883, 0.012450937441938651, 0.002918277777777777, 0.0008254666666666665, 0.003743744444444451],
    theta = categories,
    fill = 'toself',
    name = 'avg U-NSGA-III'
))

fig2.add_trace(go.Scatterpolar(
    r = [0.012075628647037762, 0.012486370859491006, 0.012357349319368289, 0.002976672203765227, 0.0010423089700996677, 0.0040189811738648995],
    theta = categories,
    fill = 'toself',
    name = 'avg C-TAEA'
))

fig2.add_trace(go.Scatterpolar(
    r = [0.013003569365913042, 0.011479399577362607, 0.013048054353292917, 0.0024428444444444452, 0.0007282111111111109, 0.0031710555555555585],
    theta = categories,
    fill = 'toself',
    name = 'avg AGE-MOEA'
))

fig2.update_layout(
    polar = dict (radialaxis = dict(
        visible = True,
        range = [0.02, -0.01]
    )),
    showlegend = True
)

fig2.show()