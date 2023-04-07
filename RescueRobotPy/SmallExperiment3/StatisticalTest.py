from re import U
from scipy.stats import mannwhitneyu
import plotly.graph_objects as go
import numpy as np
import copy

def makeStatisticalLegend(arr, dec) -> list:

    statLeg = copy.deepcopy(arr)
    for i in range(0, len(statLeg)):
        for j in range(0, len(statLeg[i])):
            if statLeg[i][j] == None:
                statLeg[i][j] = 2.0
    statLeg = np.around(statLeg, dec)
    statLegString = []
    for i in range(0, len(statLeg)):
        statLegString.append([])
        for j in range(0, len(statLeg[i])):
            if statLeg[i][j] == 2.0:
                statLegString[i].append(' ')
            else:
                statLegString[i].append(str(statLeg[i][j]))
    return statLegString
    


class StatisticalTest():

    def __init__(

        self,
        nsga3,
        unsga3,
        agemoea,
        ctaea,
        moead,
        random
    
    ):

        super(StatisticalTest, self).__init__()
        self.nsga = nsga3
        self.unsga = unsga3
        self.agemoea = agemoea
        self.ctaea = ctaea
        self.moead = moead
        self.random = random

        self.pvalue_table = [[None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None]]

        self.effect_table = [[None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None],
            [None, None, None, None, None, None]]

    def runTest(self, file_path) -> None:

        file = open(file_path, 'w')

        file.write('[RANDOM]\n')

        U1, pval = mannwhitneyu(self.nsga, self.random, method='exact')
        effect_size = U1/(len(self.nsga)*len(self.random))

        self.effect_table[5][1] = effect_size

        file.write("\t[NSGA-III]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.unsga, self.random, method='exact')
        effect_size = U1/(len(self.unsga)*len(self.random))

        self.effect_table[5][2] = effect_size

        file.write("\t[U-NSGA-III]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.agemoea, self.random, method='exact')
        effect_size = U1/(len(self.agemoea)*len(self.random))

        self.effect_table[5][3] = effect_size

        file.write("\t[AGE-MOEA]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.ctaea, self.random, method='exact')
        effect_size = U1/(len(self.ctaea)*len(self.random))

        self.effect_table[5][4] = effect_size

        file.write("\t[C-TAEA]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.moead, self.random, method='exact')
        effect_size = U1/(len(self.moead)*len(self.random))

        self.effect_table[5][5] = effect_size

        file.write("\t[MOEA-D]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        file.write('[NSGA-III]\n')

        U1, pval = mannwhitneyu(self.random, self.nsga, method='exact')
        effect_size = U1/(len(self.random)*len(self.nsga))

        self.pvalue_table[4][0] = pval
        self.effect_table[4][0] = effect_size

        file.write('\t[RANDOM]\n')
        file.write('\t\tp-value: ' + str(pval) + '\n')
        file.write('\t\teffect size: ' + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.unsga, self.nsga, method='exact')
        effect_size = U1/(len(self.unsga)*len(self.nsga))

        self.effect_table[4][2] = effect_size

        file.write("\t[U-NSGA-III]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.agemoea, self.nsga, method='exact')
        effect_size = U1/(len(self.agemoea)*len(self.nsga))

        self.effect_table[4][3] = effect_size

        file.write("\t[AGE-MOEA]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.ctaea, self.nsga, method='exact')
        effect_size = U1/(len(self.ctaea)*len(self.nsga))

        self.effect_table[4][4] = effect_size

        file.write("\t[C-TAEA]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.moead, self.nsga, method='exact')
        effect_size = U1/(len(self.moead)*len(self.nsga))

        self.effect_table[4][5] = effect_size

        file.write("\t[MOEA-D]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        file.write('[U-NSGA-III]\n')

        U1, pval = mannwhitneyu(self.random, self.unsga, method='exact')
        effect_size = U1/(len(self.random)*len(self.unsga))

        self.pvalue_table[3][0] = pval
        self.effect_table[3][0] = effect_size

        file.write('\t[RANDOM]\n')
        file.write('\t\tp-value: ' + str(pval) + '\n')
        file.write('\t\teffect size: ' + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.nsga, self.unsga, method='exact')
        effect_size = U1/(len(self.nsga)*len(self.unsga))

        self.pvalue_table[3][1] = pval
        self.effect_table[3][1] = effect_size

        file.write("\t[NSGA-III]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.agemoea, self.unsga, method='exact')
        effect_size = U1/(len(self.agemoea)*len(self.unsga))

        self.effect_table[3][3] = effect_size

        file.write("\t[AGE-MOEA]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.ctaea, self.unsga, method='exact')
        effect_size = U1/(len(self.ctaea)*len(self.unsga))

        self.effect_table[3][4] = effect_size

        file.write("\t[C-TAEA]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.moead, self.unsga, method='exact')
        effect_size = U1/(len(self.moead)*len(self.unsga))

        self.effect_table[3][5] = effect_size

        file.write("\t[MOEA-D]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        file.write('[AGE-MOEA]\n')

        U1, pval = mannwhitneyu(self.random, self.agemoea, method='exact')
        effect_size = U1/(len(self.random)*len(self.agemoea))

        self.pvalue_table[2][0] = pval
        self.effect_table[2][0] = effect_size

        file.write('\t[RANDOM]\n')
        file.write('\t\tp-value: ' + str(pval) + '\n')
        file.write('\t\teffect size: ' + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.nsga, self.agemoea, method='exact')
        effect_size = U1/(len(self.nsga)*len(self.agemoea))

        self.pvalue_table[2][1] = pval
        self.effect_table[2][1] = effect_size

        file.write("\t[NSGA-III]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.unsga, self.agemoea, method='exact')
        effect_size = U1/(len(self.unsga)*len(self.agemoea))

        self.pvalue_table[2][2] = pval
        self.effect_table[2][2] = effect_size

        file.write("\t[U-NSGA-III]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.ctaea, self.agemoea, method='exact')
        effect_size = U1/(len(self.ctaea)*len(self.agemoea))

        self.effect_table[2][4] = effect_size

        file.write("\t[C-TAEA]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.moead, self.agemoea, method='exact')
        effect_size = U1/(len(self.moead)*len(self.agemoea))

        self.effect_table[2][5] = effect_size

        file.write("\t[MOEA-D]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        file.write('[C-TAEA]\n')

        U1, pval = mannwhitneyu(self.random, self.ctaea, method='exact')
        effect_size = U1/(len(self.random)*len(self.ctaea))

        self.pvalue_table[1][0] = pval
        self.effect_table[1][0] = effect_size

        file.write('\t[RANDOM]\n')
        file.write('\t\tp-value: ' + str(pval) + '\n')
        file.write('\t\teffect size: ' + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.nsga, self.ctaea, method='exact')
        effect_size = U1/(len(self.nsga)*len(self.ctaea))

        self.pvalue_table[1][1] = pval
        self.effect_table[1][1] = effect_size

        file.write("\t[NSGA-III]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.unsga, self.ctaea, method='exact')
        effect_size = U1/(len(self.unsga)*len(self.ctaea))

        self.pvalue_table[1][2] = pval
        self.effect_table[1][2] = effect_size

        file.write("\t[U-NSGA-III]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.agemoea, self.ctaea, method='exact')
        effect_size = U1/(len(self.agemoea)*len(self.ctaea))

        self.pvalue_table[1][3] = pval
        self.effect_table[1][3] = effect_size

        file.write("\t[AGE-MOEA]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.moead, self.ctaea, method='exact')
        effect_size = U1/(len(self.moead)*len(self.ctaea))

        self.effect_table[1][5] = effect_size

        file.write("\t[MOEA-D]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        file.write('[MOEA-D]\n')

        U1, pval = mannwhitneyu(self.random, self.moead, method='exact')
        effect_size = U1/(len(self.random)*len(self.moead))

        self.pvalue_table[0][0] = pval
        self.effect_table[0][0] = effect_size

        file.write('\t[RANDOM]\n')
        file.write('\t\tp-value: ' + str(pval) + '\n')
        file.write('\t\teffect size: ' + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.nsga, self.moead, method='exact')
        effect_size = U1/(len(self.nsga)*len(self.moead))

        self.pvalue_table[0][1] = pval
        self.effect_table[0][1] = effect_size

        file.write("\t[NSGA-III]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.unsga, self.moead, method='exact')
        effect_size = U1/(len(self.unsga)*len(self.moead))

        self.pvalue_table[0][2] = pval
        self.effect_table[0][2] = effect_size

        file.write("\t[U-NSGA-III]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.agemoea, self.moead, method='exact')
        effect_size = U1/(len(self.agemoea)*len(self.moead))

        self.pvalue_table[0][3] = pval
        self.effect_table[0][3] = effect_size

        file.write("\t[AGE-MOEA]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        U1, pval = mannwhitneyu(self.ctaea, self.moead, method='exact')
        effect_size = U1/(len(self.ctaea)*len(self.moead))

        self.pvalue_table[0][4] = pval
        self.effect_table[0][4] = effect_size

        file.write("\t[C-TAEA]\n")
        file.write("\t\tp-value: " + str(pval) + '\n')
        file.write("\t\teffect size: " + str(effect_size) + '\n')

        print('Results provided in the statistical_results.txt file')

        file.close()

    def makeHeatmaps(self) -> None:

        fig1 = go.Figure(data=go.Heatmap(
                            z=self.pvalue_table,
                            x=['RANDOM', 'NSGA-3', 'U-NSGA-3', 'AGE-MOEA', 'CTAEA'],
                            y=['MOEA-D', 'CTAEA', 'AGE-MOEA', 'U-NSGA-3', 'NSGA-3'],
                            hoverongaps = False,
                            colorscale='Reds',
                            text= makeStatisticalLegend(self.pvalue_table, 3),
                            texttemplate="%{text}",
                            textfont={"size":20}))
        fig1.show()

        fig2 = go.Figure(data=go.Heatmap(
                            z=self.effect_table,
                            x=['RANDOM', 'NSGA-3', 'U-NSGA-3', 'AGE-MOEA', 'C-TAEA', 'MOEA-D'],
                            y=['MOEA-D', 'C-TAEA', 'AGE-MOEA', 'U-NSGA-3', 'NSGA-3', 'RANDOM'],
                            hoverongaps = False,
                            colorscale='Reds',
                            text=makeStatisticalLegend(self.effect_table, 3),
                            texttemplate="%{text}",
                            textfont={"size":20}))

        fig2.show()
