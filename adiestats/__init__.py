import math
import sample_sets

# averages

def mean(set_of_data):
    return sum(set_of_data)/len(set_of_data)

def median(set_of_data):
    in_order = sorted(set_of_data)
    if len(in_order)%2==1:
        median_index = int(math.ceil(len(in_order)/2)) - 1
        median = in_order[median_index]
    else:
        index_lower = int(math.ceil(len(in_order)/2)) - 1
        index_upper = int(math.ceil(len(in_order)/2))
        lower = in_order[index_lower]
        upper = in_order[index_upper]
        median = mean((lower,upper))
    return median

def mode(set_of_data):
    return max(set(set_of_data), key=set_of_data.count)

# measures of variability (1)

def range(set_of_data):
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
        q1 = mean((in_order[index_q1_lower],in_order[index_q1_upper]))
        
        index_q3_lower = int(math.ceil(len(in_order)*0.75)) - 1
        index_q3_upper = int(math.ceil(len(in_order)*0.75))
        q3 = mean((in_order[index_q3_lower],in_order[index_q3_upper]))
    return q3 - q1

# measures of variability (2): variance and standard deviation
#
# variance:

def population_variance(set_of_data):
    x = 0
    for item in set_of_data:
        x += (item-mean(set_of_data))**2
    return x/len(set_of_data)

def sample_variance(set_of_data):
    x = 0
    for item in set_of_data:
        x += (item-mean(set_of_data))**2
    return x/(len(set_of_data)-1)

# standard deviation:

def population_sd(set_of_data):
    return math.sqrt(population_variance(set_of_data))

def sample_sd(set_of_data):
    return math.sqrt(sample_variance(set_of_data))

# coefficient of variation: 

def population_cv(set_of_data):
    return population_sd(set_of_data)/mean(set_of_data)

def sample_cv(set_of_data):
    return sample_sd(set_of_data)/mean(set_of_data)

#weighted means

def pair_values(list1,list2):
    return dict(zip(list1,list2))

def weighted_mean(list1,list2):
    sum = 0
    sum_weights = 0
    paired = pair_values(list1,list2)
    for i, j in paired.items():
         sum += i*j
         sum_weights += j
    return sum/sum_weights

a = weighted_mean(sample_sets.paired_set1a, sample_sets.paired_set1b)

paired = pair_values(sample_sets.paired_set1a, sample_sets.paired_set1b)

print(a)