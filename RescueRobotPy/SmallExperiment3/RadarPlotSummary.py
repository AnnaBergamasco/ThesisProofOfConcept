
from copy import copy
import plotly.graph_objects as go


class RadarPlotSummary():

  def __init__(

    self,
    max_severities,
    avg_severities

  ):
    super(RadarPlotSummary, self).__init__()
    
    self.max_sev = copy(max_severities)
    self.avg_sev = copy(avg_severities)

  
  def makePlot(self) -> None:

    categories = ['S0 e1 S1','S0 e1 S2', 'S0 e1 S6', 'S3 e1 S1', 'S3 e1 S4', 'S3 e1 S5']

    

    fig1 = go.Figure()

    fig1.add_trace(go.Scatterpolar(
          r= self.max_sev[0],
          theta=categories,
          fill='none',
          name='NSGA-III'
    ))
    
    fig1.add_trace(go.Scatterpolar(
          r= self.max_sev[1],
          theta=categories,
          fill='none',
          name='U-NSGA-III'
    ))

    fig1.add_trace(go.Scatterpolar(
          r= self.max_sev[2],
          theta=categories,
          fill='none',
          name='AGE-MOEA'
    ))

    fig1.add_trace(go.Scatterpolar(
          r= self.max_sev[3],
          theta=categories,
          fill='none',
          name='C-TAEA'
    ))

    fig1.add_trace(go.Scatterpolar(
          r= self.max_sev[4],
          theta=categories,
          fill='none',
          name='MOEA-D'
    ))

    fig1.add_trace(go.Scatterpolar(
          r= self.max_sev[5],
          theta=categories,
          fill='none',
          name='RANDOM'
    ))

    fig1.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0.0, 1.0]
        )),
      showlegend=True
    )

    fig1.show()

    fig2 = go.Figure()

    fig2.add_trace(go.Scatterpolar(
          r= self.avg_sev[0],
          theta=categories,
          fill='none',
          name='NSGA-III'
    ))
    
    fig2.add_trace(go.Scatterpolar(
          r= self.avg_sev[1],
          theta=categories,
          fill='none',
          name='U-NSGA-III'
    ))

    fig2.add_trace(go.Scatterpolar(
          r= self.avg_sev[2],
          theta=categories,
          fill='none',
          name='AGE-MOEA'
    ))

    fig2.add_trace(go.Scatterpolar(
          r= self.avg_sev[3],
          theta=categories,
          fill='none',
          name='C-TAEA'
    ))

    fig2.add_trace(go.Scatterpolar(
          r= self.avg_sev[4],
          theta=categories,
          fill='none',
          name='MOEA-D'
    ))

    fig2.add_trace(go.Scatterpolar(
          r= self.avg_sev[5],
          theta=categories,
          fill='none',
          name='RANDOM'
    ))

    fig2.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0.0, 1.0]
        )),
      showlegend=True
    )

    fig2.show()