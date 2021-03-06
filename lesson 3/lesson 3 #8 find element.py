# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(p, target):
    i = 0
    for e in p:
        i = i + 1
        if e == target:
            return i - 1
    return -1


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1


#We could also use while loop

def find_element(p, target):
    i = 0
    while i < len(p):
        if p[i] == target:
            return i
        i = i + 1
    return -1


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
