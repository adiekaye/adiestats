'''
Created on Jun 29, 2015

@author: adiekaye
'''

from . import ave
from . import var
from . import data_processes as proc

def cov (xs, ys, data_type = "sample"):
    n = len(xs) - 1
    sum = 0
    if data_type == "population":
        n += 1
    mu_x = ave.mean(xs)
    mu_y = ave.mean(ys)
    paired = proc.pair_values(xs,ys)
    for x,y in paired.items():
        sum += (x-mu_x)*(y-mu_y)
    return sum/n

def cor (xs, ys, data_type = "sample"):
    return cov(xs,ys,data_type)/(var.sd(xs,data_type)*var.sd(ys,data_type))