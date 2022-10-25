from re import U
from scipy.stats import mannwhitneyu

nsga = [48, 90, 12, 80, 86, 43, 32, 65, 21, 0, 118, 98, 108, 11, 59, 57, 17, 18, 33, 77]
unsga = [37, 2, 95, 53, 38, 34, 77, 89, 80, 31, 69, 31, 19, 40, 68, 10, 36, 19, 66, 30]
agemoea = [178, 178, 188, 168, 175, 162, 204, 212, 162, 188, 0, 180, 96, 181, 202, 180, 197, 133, 191, 128]
ctaea = [106, 100, 97, 62, 100, 42, 104, 80, 14, 42, 92, 0, 137, 118, 117, 112, 127, 117, 115, 123]
random = [1, 0, 1, 0, 2, 1, 1, 2, 0, 0, 1, 1, 0, 0, 1, 0, 2, 0, 0, 2]

U1, pval = mannwhitneyu(nsga, random, method='exact')
effect_size = U1/(len(nsga)*len(random))

print("NSGA-III:")
print("\tU: " + str(U1))
print("\tp-value: " + str(pval))
print("\teffect size: " + str(effect_size))

U1, pval = mannwhitneyu(unsga, random, method='exact')
effect_size = U1/(len(unsga)*len(random))

print("U-NSGA-III:")
print("\tU: " + str(U1))
print("\tp-value: " + str(pval))
print("\teffect size: " + str(effect_size))

U1, pval = mannwhitneyu(agemoea, random, method='exact')
effect_size = U1/(len(agemoea)*len(random))

print("AGE-MOEA:")
print("\tU: " + str(U1))
print("\tp-value: " + str(pval))
print("\teffect size: " + str(effect_size))

U1, pval = mannwhitneyu(ctaea, random, method='exact')
effect_size = U1/(len(ctaea)*len(random))

print("C-TAEA:")
print("\tU: " + str(U1))
print("\tp-value: " + str(pval))
print("\teffect size: " + str(effect_size))
