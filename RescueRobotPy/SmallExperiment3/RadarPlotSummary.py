
from copy import copy
import plotly.express as px
import pandas as pd


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

    theta = categories + categories + categories + categories + categories + categories

    rfig1 = self.max_sev[0] + self.max_sev[1] + self.max_sev[2] +self.max_sev[3] +self.max_sev[4] +self.max_sev[5]
    rfig2 = self.avg_sev[0] + self.avg_sev[1] + self.avg_sev[2] +self.avg_sev[3] +self.avg_sev[4] +self.avg_sev[5]

    color = ['NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III',
      'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III',
      'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA',
      'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA',
      'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD',
      'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM']

    df1 = pd.DataFrame(dict(
      color=color,
      r= rfig1,
      theta=theta))
    

    fig1 = px.line_polar(df1, r='r', theta='theta', color='color', line_close=True)
    
    
    fig1.show()

    df2 = pd.DataFrame(dict(
      color=color,
      r= rfig2,
      theta=theta))
    

    fig2 = px.line_polar(df2, r='r', theta='theta', color='color', line_close=True)
    
    
    fig2.show()