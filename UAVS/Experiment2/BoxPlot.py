import plotly.graph_objects as go

class BoxPlotVariables():

    def __init__(
        self,
        nsga3,
        unsga3,
        agemoea,
        ctaea,
        moead,
        random
    ):
        super(BoxPlotVariables, self).__init__()

        self.nsga3 = nsga3
        self.unsga3 = unsga3
        self.agemoea = agemoea
        self.ctaea = ctaea
        self.moead = moead
        self.random = random
    
    def makePlot(self) -> None:
        
        fig = go.Figure()

        fig.add_trace(go.Box(y=self.nsga3,
                    name="NSGA-III"
                    ))

        fig.add_trace(go.Box(y=self.unsga3,
                    name="U-NSGA-III"
                    ))

        fig.add_trace(go.Box(y=self.agemoea,
                    name="AGE-MOEA"
                    ))

        fig.add_trace(go.Box(y=self.ctaea,
                    name="C-TAEA"
                    ))

        fig.add_trace(go.Box(y=self.moead,
                    name="MOEA-D"
                    ))

        fig.add_trace(go.Box(y=self.random,
                    name="RANDOM"
                    ))

        fig.update_traces(boxpoints='all', jitter=0)
        fig.show()




