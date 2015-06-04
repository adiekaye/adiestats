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
