
from copy import copy
import plotly.graph_objects as go


class RadarPlotAlgorithms():

  def __init__(

    self,
    max_sev_low_bounds,
    max_sev_hi_bounds,
    avg_sev_low_bounds,
    avg_sev_hi_bounds

  ):
    super(RadarPlotAlgorithms, self).__init__()
    
    self.max_sev_low_bounds = copy(max_sev_low_bounds)
    self.max_sev_hi_bounds = copy(max_sev_hi_bounds)
    self.avg_sev_low_bounds = copy(avg_sev_low_bounds)
    self.avg_sev_hi_bounds = copy(avg_sev_hi_bounds)

  
  def makePlot(self) -> None:

    categories = ['S0 e1 S1','S0 e1 S2', 'S0 e1 S6', 'S3 e1 S1', 'S3 e1 S4', 'S3 e1 S5']

    

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
          r= self.max_sev_low_bounds,
          theta=categories,
          fill='none',
          name='maximum severity lower bounds'
    ))
    
    fig.add_trace(go.Scatterpolar(
          r= self.max_sev_hi_bounds,
          theta=categories,
          fill='none',
          name='maximum severity higher bounds'
    ))

    fig.add_trace(go.Scatterpolar(
          r= self.avg_sev_low_bounds,
          theta=categories,
          fill='none',
          name='average severity lower bounds'
    ))

    fig.add_trace(go.Scatterpolar(
          r= self.avg_sev_hi_bounds,
          theta=categories,
          fill='none',
          name='average severity higher bounds'
    ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0.0, 1.0]
        )),
      showlegend=True
    )

    fig.show()