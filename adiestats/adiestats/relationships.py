'''
Created on Jun 29, 2015

@author: adiekaye
'''

import math
from . import ave
from . import var
from . import data_processes as proc

#finding covariance of two variables x and y

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

#finding the correlation coefficient of two variables x and y

def cor (xs, ys, data_type = "sample"):
    return cov(xs,ys,data_type)/(var.sd(xs,data_type)*var.sd(ys,data_type))

#is there a relationship?

def get_relationship(xs, ys, data_type = "sample"):
    r = cor(xs,ys,data_type)
    n = len(xs)
    print(r)
    abs_r = math.fabs(r)
    print(abs_r)
    check = 2/math.sqrt(n)
    print(check)
    if r == 0:
        return "There is no relationship"
    strength ="weak"
    direction = "negative"
    if abs_r >= check:
        strength = "strong"
    if r>0:
        direction = "positive"
    return "There is a %s %s relationship (%f vs %f) between x and y" % (strength, direction, abs_r, check)

#least squares regression

"""
def least_squares_regr(xs, ys, data_type="sample"):
    b1 = 
    b2 =
    return b1, b2
"""