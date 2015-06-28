import math
from . import ave
from . import data_processes as proc

# measures of variability (1)

def var_range(set_of_data):
    return max(set_of_data) - min(set_of_data)

def iqr(set_of_data):
    in_order = sorted(set_of_data) 
    if len(in_order)%4>0:
        index_q1 = int(math.ceil(len(in_order)*0.25)) - 1
        q1 = in_order[index_q1]
        index_q3 = int(math.ceil(len(in_order)*0.75)) - 1
        q3 = in_order[index_q3]
    else:
        index_q1_lower = int(math.ceil(len(in_order)*0.25)) - 1
        index_q1_upper = int(math.ceil(len(in_order)*0.25))
        q1 = ave.mean((in_order[index_q1_lower],in_order[index_q1_upper]))
        
        index_q3_lower = int(math.ceil(len(in_order)*0.75)) - 1
        index_q3_upper = int(math.ceil(len(in_order)*0.75))
        q3 = ave.mean((in_order[index_q3_lower],in_order[index_q3_upper]))
    return q3 - q1

# measures of variability (2): variance and standard deviation
#
# variance:

def variance(set_of_data, data_type = "sample"):
    x = 0
    n = len(set_of_data)-1
    if data_type == "population":
        n += 1
    for item in set_of_data:
        x += (item-ave.mean(set_of_data))**2
    return x/n

# standard deviation:

def sd(set_of_data, data_type = "sample"):
    return math.sqrt(variance(set_of_data, data_type))

# coefficient of variation: 

def cv(set_of_data, data_type = "sample"):
    return sd(set_of_data, data_type)/ave.mean(set_of_data)

#approximate variance and standard deviation for grouped data

def var_grouped(values,frequencies,data_type = "sample"):
    x = 0
    n = 0
    mu = ave.mean_grouped(values,frequencies)
    paired = proc.pair_values(values,frequencies)
    for m,f in paired.items():
        x += f*(m-mu)**2
        n += f
    if data_type == "sample":
        n -= 1
    return x/n

def sd_grouped(values, frequencies, data_type = "sample"):
    return math.sqrt(var_grouped(values, frequencies, data_type))