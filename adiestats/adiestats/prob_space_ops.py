'''
Created on Jun 30, 2015

Probability space operators

@author: adiekaye
'''

#calculating union of 1 or more spaces (as lists:

def union(*args):
    output = set([])
    for x in args:
        output = output|set(x)
    return list(output)

#calculating intersection / joint probability of 1 or more spaces (as lists:

def joint(*args):
    output = set(args[0])
    for x in args:
        output = output&set(x)
    return list(output)

#testing for mutual exclusivity between two events as lists:

def are_mutually_exclusive(A,B):
    if joint(A,B)==[]:
        return True
    else:
        return False
    
#testing for collective exhaustion of a list of events compared to a sample space, S:

def are_collectively_exhaustive(S, *args):
    E = union(*args)
    if E==S:
        return True
    else:
        return False
    
    
x = [1,2,3]
y = [3]
z = [1,2]
w = range(10)

print(are_collectively_exhaustive(x,y))


