#examples for using the relationships module

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import adiestats
from data import sample_sets as data

a = adiestats.relationships.cov(data.x,data.y)
print(a)
b = adiestats.relationships.cor(data.x,data.y)
print(b)