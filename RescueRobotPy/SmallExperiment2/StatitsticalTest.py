from re import U
from scipy.stats import mannwhitneyu

nsga = [48, 90, 12, 80, 86, 43, 32, 65, 21, 0, 118, 98, 108, 11, 59, 57, 17, 18, 33, 77]
unsga = [37, 2, 95, 53, 38, 34, 77, 89, 80, 31, 69, 31, 19, 40, 68, 10, 36, 19, 66, 30]
agemoea = [178, 178, 188, 168, 175, 162, 204, 212, 162, 188, 0, 180, 96, 181, 202, 180, 197, 133, 191, 128]
ctaea = [106, 100, 97, 62, 100, 42, 104, 80, 14, 42, 92, 0, 137, 118, 117, 112, 127, 117, 115, 123]
random = [1, 0, 1, 0, 2, 1, 1, 2, 0, 0, 1, 1, 0, 0, 1, 0, 2, 0, 0, 2]
moead = [0, 486, 0, 0, 0, 0, 593, 0, 190, 0, 0, 0, 0, 0, 0, 470, 0, 0, 0, 0]

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