# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(p):
    if p == []:
        return 0
    else:
        bigger = p[0]
        for e in p:
            if e > bigger:
                bigger = e
        return bigger
        
            
print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0



# An easy version 

def greatest(p):
    bigger = 0
    for e in p:
        if e > bigger:
            bigger = e
    return bigger
        
            
print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
