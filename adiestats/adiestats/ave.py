from . import data_processes as proc

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

#weighted means

def weighted_mean(values,weights):
    sum = 0
    sum_weights = 0
    paired = proc.pair_values(values,weights)
    for value, weight in paired.items():
        sum += value*weight
        sum_weights += weight
    return sum/sum_weights

#approximate mean for grouped data

def mean_grouped(means,frequencies):
    return weighted_mean(means,frequencies)

#generating a geometric mean, or 'growth rate'

def geometric_mean(xs):
    n = len(xs)
    product = 1
    for x in xs:
        product *= x
    return product**(1/n)

