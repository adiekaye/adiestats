#examples for using the relationships module

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import adiestats
from data import sample_sets as data

a = adiestats.relationships.cov(data.x,data.y,"population")
print(a)
b = adiestats.relationships.cor(data.x,data.y,"sample")
print(b)

c = adiestats.relationships.cor(data.temperature,data.sales,"population")
print(c)

d = adiestats.relationships.get_relationship(data.x,data.y)
print(d)

e = adiestats.relationships.least_squares_regr(data.x,data.y)
print(e)