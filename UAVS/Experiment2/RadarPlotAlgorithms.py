
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

    categories = ['S0 sTrt S1', 'S0 sTrt S21', 'S0 sTrt S22', 'S7 sTrt S6', 'S7 sTrt S8', 'S7 sTrt S21', 'S7 sTrt S22', 'S14 sTrt S13', 'S14 sTrt S15', 'S14 sTrt S21', 'S14 sTrt S22', 'S20 sTrt S19', 'S20 sTrt S21', 'S20 sTrt S22']
    theta = categories + categories + categories + categories
    color = ['max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound', 'max severity low bound',
        'max severity hi bound','max severity hi bound','max severity hi bound','max severity hi bound','max severity hi bound','max severity hi bound', 'max severity hi bound','max severity hi bound','max severity hi bound','max severity hi bound','max severity hi bound','max severity hi bound', 'max severity hi bound','max severity hi bound',
        'avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound','avg severity low bound',
        'avg severity hi bound','avg severity hi bound','avg severity hi bound','avg severity hi bound','avg severity hi bound','avg severity hi bound', 'avg severity hi bound','avg severity hi bound','avg severity hi bound','avg severity hi bound','avg severity hi bound','avg severity hi bound', 'avg severity hi bound','avg severity hi bound']
    r = self.max_sev_low_bounds + self.max_sev_hi_bounds + self.avg_sev_low_bounds + self.avg_sev_hi_bounds
    
    df = pd.DataFrame(dict(
      color=color,
      r= r,
      theta=theta))
    

    fig = px.line_polar(df, r='r', theta='theta', color='color', line_close=True)
    
    
    fig.show()