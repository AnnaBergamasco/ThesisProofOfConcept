
from copy import copy
import plotly.graph_objects as go


class RadarPlot():

  def __init__(

    self,
    min_low_bounds,
    min_hi_bounds,
    avg_low_bounds,
    avg_hi_bounds

  ):
    super(RadarPlot, self).__init__()
    
    self.min_low_bounds = copy(min_low_bounds)
    self.min_hi_bounds = copy(min_hi_bounds)
    self.avg_low_bounds = copy(avg_low_bounds)
    self.avg_hi_bounds = copy(avg_hi_bounds)

    for i in range(0, 6):
      self.min_low_bounds[i] = -self.min_low_bounds[i]
      self.min_hi_bounds[i] = -self.min_hi_bounds[i]
      self.avg_low_bounds[i] = -self.avg_low_bounds[i]
      self.avg_hi_bounds[i] = -self.avg_hi_bounds[i]

  def makePlot(self) -> None:

    categories = ['S0 e1 S1','S0 e1 S2', 'S0 e1 S6', 'S3 e1 S1', 'S3 e1 S4', 'S3 e1 S5']

    

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
          r= self.min_low_bounds,
          theta=categories,
          fill='toself',
          name='minimum lower bounds'
    ))
    
    fig.add_trace(go.Scatterpolar(
          r= self.min_hi_bounds,
          theta=categories,
          fill='toself',
          name='minimum higher bounds'
    ))

    fig.add_trace(go.Scatterpolar(
          r= self.avg_low_bounds,
          theta=categories,
          fill='toself',
          name='average lower bounds'
    ))

    fig.add_trace(go.Scatterpolar(
          r= self.avg_hi_bounds,
          theta=categories,
          fill='toself',
          name='average higher bounds'
    ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[-0.02, 0.01]
        )),
      showlegend=True
    )

    fig.show()