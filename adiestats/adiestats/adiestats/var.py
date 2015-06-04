import math
import ave

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

def population_variance(set_of_data):
    x = 0
    for item in set_of_data:
        x += (item-ave.mean(set_of_data))**2
    return x/len(set_of_data)

def sample_variance(set_of_data):
    x = 0
    for item in set_of_data:
        x += (item-ave.mean(set_of_data))**2
    return x/(len(set_of_data)-1)

# standard deviation:

def population_sd(set_of_data):
    return math.sqrt(population_variance(set_of_data))

def sample_sd(set_of_data):
    return math.sqrt(sample_variance(set_of_data))

# coefficient of variation: 

def population_cv(set_of_data):
    return population_sd(set_of_data)/ave.mean(set_of_data)

def sample_cv(set_of_data):
    return sample_sd(set_of_data)/ave.mean(set_of_data)