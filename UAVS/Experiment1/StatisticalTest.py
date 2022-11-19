from re import U
from scipy.stats import mannwhitneyu

nsga = [776, 652, 627, 481, 639, 658, 542, 841, 494, 887, 664, 774, 603, 571, 555, 665, 888, 575, 732]
unsga = [653, 617, 393, 467, 754, 647, 342, 529, 491, 658, 695, 401, 845, 646, 639, 642, 537, 616, 742, 755]
agemoea = [1304, 968, 1156, 1242, 1243, 1104, 817, 1153, 1246, 1410, 1438, 1295, 1070, 1336, 1016, 1199, 940, 1373, 1256, 1089]
ctaea = [1649, 1461, 1296, 1567, 1230, 1404, 1744, 1660, 1315, 288, 1239, 1348, 1688, 1488, 1165, 1249, 1913, 1795, 1651, 1416]
moead = [3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
random = [9, 8, 5, 6, 6, 8, 5, 4, 7, 9, 10, 7, 9, 6, 6, 7, 6, 6, 10, 8]

file = open('statistical_results.txt', 'w')

file.write('[RANDOM]\n')

U1, pval = mannwhitneyu(nsga, random, method='exact')
effect_size = U1/(len(nsga)*len(random))

file.write("\t[NSGA-III]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(unsga, random, method='exact')
effect_size = U1/(len(unsga)*len(random))

file.write("\t[U-NSGA-III]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(agemoea, random, method='exact')
effect_size = U1/(len(agemoea)*len(random))

file.write("\t[AGE-MOEA]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(ctaea, random, method='exact')
effect_size = U1/(len(ctaea)*len(random))

file.write("\t[C-TAEA]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(moead, random, method='exact')
effect_size = U1/(len(moead)*len(random))

file.write("\t[MOEA-D]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

file.write('[NSGA-III]\n')

U1, pval = mannwhitneyu(random, nsga, method='exact')
effect_size = U1/(len(random)*len(nsga))

file.write('\t[RANDOM]\n')
file.write('\t\tp-value: ' + str(pval) + '\n')
file.write('\t\teffect size: ' + str(effect_size) + '\n')

U1, pval = mannwhitneyu(unsga, nsga, method='exact')
effect_size = U1/(len(unsga)*len(nsga))

file.write("\t[U-NSGA-III]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(agemoea, nsga, method='exact')
effect_size = U1/(len(agemoea)*len(nsga))

file.write("\t[AGE-MOEA]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(ctaea, nsga, method='exact')
effect_size = U1/(len(ctaea)*len(nsga))

file.write("\t[C-TAEA]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(moead, nsga, method='exact')
effect_size = U1/(len(moead)*len(nsga))

file.write("\t[MOEA-D]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

file.write('[U-NSGA-III]\n')

U1, pval = mannwhitneyu(random, unsga, method='exact')
effect_size = U1/(len(random)*len(unsga))

file.write('\t[RANDOM]\n')
file.write('\t\tp-value: ' + str(pval) + '\n')
file.write('\t\teffect size: ' + str(effect_size) + '\n')

U1, pval = mannwhitneyu(nsga, unsga, method='exact')
effect_size = U1/(len(nsga)*len(unsga))

file.write("\t[NSGA-III]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(agemoea, unsga, method='exact')
effect_size = U1/(len(agemoea)*len(unsga))

file.write("\t[AGE-MOEA]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(ctaea, unsga, method='exact')
effect_size = U1/(len(ctaea)*len(unsga))

file.write("\t[C-TAEA]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(moead, unsga, method='exact')
effect_size = U1/(len(moead)*len(unsga))

file.write("\t[MOEA-D]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

file.write('[AGE-MOEA]\n')

U1, pval = mannwhitneyu(random, agemoea, method='exact')
effect_size = U1/(len(random)*len(agemoea))

file.write('\t[RANDOM]\n')
file.write('\t\tp-value: ' + str(pval) + '\n')
file.write('\t\teffect size: ' + str(effect_size) + '\n')

U1, pval = mannwhitneyu(nsga, agemoea, method='exact')
effect_size = U1/(len(nsga)*len(agemoea))

file.write("\t[NSGA-III]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(unsga, agemoea, method='exact')
effect_size = U1/(len(unsga)*len(agemoea))

file.write("\t[U-NSGA-III]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(ctaea, agemoea, method='exact')
effect_size = U1/(len(ctaea)*len(agemoea))

file.write("\t[C-TAEA]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(moead, agemoea, method='exact')
effect_size = U1/(len(moead)*len(agemoea))

file.write("\t[MOEA-D]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

file.write('[C-TAEA]\n')

U1, pval = mannwhitneyu(random, ctaea, method='exact')
effect_size = U1/(len(random)*len(ctaea))

file.write('\t[RANDOM]\n')
file.write('\t\tp-value: ' + str(pval) + '\n')
file.write('\t\teffect size: ' + str(effect_size) + '\n')

U1, pval = mannwhitneyu(nsga, ctaea, method='exact')
effect_size = U1/(len(nsga)*len(ctaea))

file.write("\t[NSGA-III]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(unsga, ctaea, method='exact')
effect_size = U1/(len(unsga)*len(ctaea))

file.write("\t[U-NSGA-III]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(agemoea, ctaea, method='exact')
effect_size = U1/(len(agemoea)*len(ctaea))

file.write("\t[AGE-MOEA]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(moead, ctaea, method='exact')
effect_size = U1/(len(moead)*len(ctaea))

file.write("\t[MOEA-D]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

file.write('[MOEA-D]\n')

U1, pval = mannwhitneyu(random, moead, method='exact')
effect_size = U1/(len(random)*len(moead))

file.write('\t[RANDOM]\n')
file.write('\t\tp-value: ' + str(pval) + '\n')
file.write('\t\teffect size: ' + str(effect_size) + '\n')

U1, pval = mannwhitneyu(nsga, moead, method='exact')
effect_size = U1/(len(nsga)*len(moead))

file.write("\t[NSGA-III]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(unsga, moead, method='exact')
effect_size = U1/(len(unsga)*len(moead))

file.write("\t[U-NSGA-III]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(agemoea, moead, method='exact')
effect_size = U1/(len(agemoea)*len(moead))

file.write("\t[AGE-MOEA]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

U1, pval = mannwhitneyu(ctaea, moead, method='exact')
effect_size = U1/(len(ctaea)*len(moead))

file.write("\t[C-TAEA]\n")
file.write("\t\tp-value: " + str(pval) + '\n')
file.write("\t\teffect size: " + str(effect_size) + '\n')

print('Results provided in the statistical_results.txt file')

file.close()