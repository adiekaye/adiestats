import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from adiestats import ave, sample_sets, var

a = ave.weighted_mean(sample_sets.paired_set1a, sample_sets.paired_set1b)

print(a)

b = var.cv(sample_sets.set5)

print(b)