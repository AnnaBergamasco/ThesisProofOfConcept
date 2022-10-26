
from asyncio import SafeChildWatcher
from audioop import avg
from copy import copy
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
from itertools import chain

categories = ['S0 e1 S1','S0 e1 S2', 'S0 e1 S6', 'S3 e1 S1', 'S3 e1 S4', 'S3 e1 S5']

fig1 = go.Figure()

minRANDOM = [-0.007598670378823384, 0.005475649037884112, -0.003046069529013114, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]
minNSGA3 = [-0.007583341070633805, 0.008018893859577103, -0.002844446101142129, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]
minUNSGA3 = [-0.007583450823347492, 0.008536780363509577, -0.0028457821000263993, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]
minCTAEA = [-0.007583365616792707, 0.008974595093018678, -0.002834976383143386, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]
minAGEMOEA = [-0.007583333726698659, 0.009112849124759625, -0.002831590069578596, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]
minMOEAD = [-0.007583333352022664, 0.009112870138011098, -0.0028311057217337184, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]

minValues = [minRANDOM, minNSGA3, minUNSGA3, minCTAEA, minAGEMOEA, minMOEAD]

avgRANDOM = [-0.012901185107996272, -0.019315010413081438, -0.00900041262478597, -0.003779911111111111, -0.0012781444444444443, -0.005058055555555566]
avgNSGA3 = [-0.012067100446369862, -0.014719300232457709, -0.012253217085680003, -0.0028643055555555557, -0.000846461111111111, -0.003710766666666673]
avgUNSGA3 = [-0.012153637068077055, -0.014185063778808883, -0.012450937441938651, -0.002918277777777777, -0.0008254666666666665, -0.003743744444444451]
avgCTAEA = [-0.012075628647037762, -0.012486370859491006, -0.012357349319368289, -0.002976672203765227, -0.0010423089700996677, -0.0040189811738648995]
avgAGEMOEA = [-0.013003569365913042, -0.011479399577362607, -0.013048054353292917, -0.0024428444444444452, -0.0007282111111111109, -0.0031710555555555585]
avgMOEAD = [-0.011335967106192134, -0.014156274558110884, -0.007217672360829588, -0.0035046707589285703, -0.000764933035714286, -0.004269603794642866]

avgValues = [avgRANDOM, avgNSGA3, avgUNSGA3, avgCTAEA, avgAGEMOEA, avgMOEAD]

maxRANDOM = [-0.00832366367654425, -0.00536216189419747, -0.003791181407659869, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]
maxNSGA3 = [-0.00888343089937076, -0.00022660973959387487, -0.005006608559038089, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]
maxUNSGA3 = [-0.008167688508913713, 0.002362777870604238, -0.003953557298686003, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]
maxCTAEA = [-0.009864628571415322, 0.005067861308424848, -0.00544545129103369, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]
maxAGEMOEA = [-0.007683344392174712, 0.008126892252376727, -0.003500266762905313, -9.99999999999994e-05, -0.0, -9.999999999998899e-05]
maxMOEAD = [-0.009858079647716386, -0.015044053285287684, -0.005174612106262479, -0.0005000000000000004, -0.0, -0.000500000000000056]

maxValues = [maxRANDOM, maxNSGA3, maxUNSGA3, maxCTAEA, maxAGEMOEA, maxMOEAD]

scaler = MinMaxScaler()
scaler.fit(minValues)
minValues = scaler.transform(minValues)

scaler = MinMaxScaler()
scaler.fit(avgValues)
avgValues = scaler.transform(avgValues)

scaler = MinMaxScaler()
scaler.fit(maxValues)
maxValues = scaler.transform(maxValues)

minRANDOM = minValues[0]
minNSGA3 = minValues[1]
minUNSGA3 = minValues[2]
minCTAEA = minValues[3]
minAGEMOEA = minValues[4]
minMOEAD = minValues[5]

avgRANDOM = avgValues[0]
avgNSGA3 = avgValues[1]
avgUNSGA3 = avgValues[2]
avgCTAEA = avgValues[3]
avgAGEMOEA = avgValues[4]
avgMOEAD = avgValues[5]

maxRANDOM = maxValues[0]
maxNSGA3 = maxValues[1]
maxUNSGA3 = maxValues[2]
maxCTAEA = maxValues[3]
maxAGEMOEA = maxValues[4]
maxMOEAD = maxValues[5]

fig1.add_trace(go.Scatterpolar(
    r =
    minRANDOM,
    theta = categories,
    fill = 'none',
    name = 'min RANDOM'
))

fig1.add_trace(go.Scatterpolar(
    r = minNSGA3,
    theta = categories,
    fill = 'none',
    name = 'min NSGA-III'
))

fig1.add_trace(go.Scatterpolar(
    r = minUNSGA3,
    theta = categories,
    fill = 'none',
    name = 'min U-NSGA-III'
))

fig1.add_trace(go.Scatterpolar(
    r = minCTAEA,
    theta = categories,
    fill = 'none',
    name = 'min C-TAEA'
))

fig1.add_trace(go.Scatterpolar(
    r = minAGEMOEA,
    theta = categories,
    fill = 'none',
    name = 'min AGE-MOEA'
))

fig1.add_trace(go.Scatterpolar(
    r = minMOEAD,
    theta = categories,
    fill = 'none',
    name = 'min MOEA-D'
))


fig1.update_layout(
    polar = dict (
        radialaxis = dict(
            visible = True,
            range = [0.0, 1.0]
            )),
    showlegend = True,
)

fig1.show()

fig2 = go.Figure()

fig2.add_trace(go.Scatterpolar(
    r = avgRANDOM,
    theta = categories,
    fill = 'none',
    name = 'avg RANDOM'
))

fig2.add_trace(go.Scatterpolar(
    r = avgNSGA3,
    theta = categories,
    fill = 'none',
    name = 'avg NSGA-III'
))

fig2.add_trace(go.Scatterpolar(
    r = avgUNSGA3,
    theta = categories,
    fill = 'none',
    name = 'avg U-NSGA-III'
))

fig2.add_trace(go.Scatterpolar(
    r = avgCTAEA,
    theta = categories,
    fill = 'none',
    name = 'avg C-TAEA'
))

fig2.add_trace(go.Scatterpolar(
    r = avgAGEMOEA,
    theta = categories,
    fill = 'none',
    name = 'avg AGE-MOEA'
))

fig2.add_trace(go.Scatterpolar(
    r = avgMOEAD,
    theta = categories,
    fill = 'none',
    name = 'avg MOEA-D'
))

fig2.update_layout(
    polar = dict (radialaxis = dict(
        visible = True,
        range = [0.0, 1.0]
    )),
    showlegend = True
)

fig2.show()

fig3 = go.Figure()

fig3.add_trace(go.Scatterpolar(
    r = maxRANDOM,
    theta = categories,
    fill = 'none',
    name = 'max RANDOM'
))

fig3.add_trace(go.Scatterpolar(
    r = maxNSGA3,
    theta = categories,
    fill = 'none',
    name = 'max NSGA-III'
))

fig3.add_trace(go.Scatterpolar(
    r = maxUNSGA3,
    theta = categories,
    fill = 'none',
    name = 'max U-NSGA-III'
))

fig3.add_trace(go.Scatterpolar(
    r = maxCTAEA,
    theta = categories,
    fill = 'none',
    name = 'max C-TAEA'
))

fig3.add_trace(go.Scatterpolar(
    r = maxAGEMOEA,
    theta = categories,
    fill = 'none',
    name = 'max AGE-MOEA'
))

fig3.add_trace(go.Scatterpolar(
    r = maxMOEAD,
    theta = categories,
    fill = 'none',
    name = 'max MOEA-D'
))

fig3.update_layout(
    polar = dict (radialaxis = dict(
        visible = True,
        range = [0.0, 1.0]
    )),
    showlegend = True
)

fig3.show()