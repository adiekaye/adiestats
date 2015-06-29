#examples for using the averages and variability modules

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import adiestats
from data import sample_sets as data

a = adiestats.ave.weighted_mean(data.paired_set1a, data.paired_set1b)

print(a)

b = adiestats.var.cv(data.set5)

print(b)

c = adiestats.ave.mean_grouped(data.m,data.f)
print(c)

c = adiestats.var.sd_grouped(data.m,data.f)
print(c)

d = adiestats.ave.geometric_mean(data.growths)
print(d)