import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import adiestats

a = adiestats.ave.weighted_mean(adiestats.sample_sets.paired_set1a, adiestats.sample_sets.paired_set1b)

print(a)

b = adiestats.var.cv(adiestats.sample_sets.set5)

print(b)

c = adiestats.ave.mean_grouped(adiestats.sample_sets.m,adiestats.sample_sets.f)
print(c)

c = adiestats.var.sd_grouped(adiestats.sample_sets.m,adiestats.sample_sets.f)
print(c)
