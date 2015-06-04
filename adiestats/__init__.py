import math
import sample_sets
import ave
import var

a = ave.weighted_mean(sample_sets.paired_set1a, sample_sets.paired_set1b)

print(a)

b = var.sample_cv(sample_sets.set5)

print(b)