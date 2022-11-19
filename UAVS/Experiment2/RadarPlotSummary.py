
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

    categories = ['S0 sTrt S1', 'S0 sTrt S21', 'S0 sTrt S22', 'S7 sTrt S6', 'S7 sTrt S8', 'S7 sTrt S21', 'S7 sTrt S22', 'S14 sTrt S13', 'S14 sTrt S15', 'S14 sTrt S21', 'S14 sTrt S22', 'S20 sTrt S19', 'S20 sTrt S21', 'S20 sTrt S22']

    theta = categories + categories + categories + categories + categories + categories

    rfig1 = self.max_sev[0] + self.max_sev[1] + self.max_sev[2] +self.max_sev[3] +self.max_sev[4] +self.max_sev[5]
    rfig2 = self.avg_sev[0] + self.avg_sev[1] + self.avg_sev[2] +self.avg_sev[3] +self.avg_sev[4] +self.avg_sev[5]

    color = ['NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III', 'NSGA-III',
      'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III', 'U-NSGA-III',
      'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA', 'AGE-MOEA',
      'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA', 'C-TAEA',
      'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD', 'MOEAD',
      'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM', 'RANDOM']

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