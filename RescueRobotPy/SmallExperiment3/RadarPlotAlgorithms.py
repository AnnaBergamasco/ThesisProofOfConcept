
from copy import copy
import plotly.express as px
import pandas as pd


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
    theta = categories + categories + categories + categories
    color = ['max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound',
        'max severity hi bound','max severity hi bound','max severity hi bound','max severity hi bound','max severity hi bound','max severity hi bound',
        'avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound',
        'avg severity hi bound','avg severity hi bound','avg severity hi bound','avg severity hi bound','avg severity hi bound','avg severity hi bound']
    r = self.max_sev_low_bounds + self.max_sev_hi_bounds + self.avg_sev_low_bounds + self.avg_sev_hi_bounds
    
    df = pd.DataFrame(dict(
      color=color,
      r= r,
      theta=theta))
    

    fig = px.line_polar(df, r='r', theta='theta', color='color', line_close=True)
    
    
    fig.show()
