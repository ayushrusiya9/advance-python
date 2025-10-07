# map higher order isiliye iske ander ek function pass krenge
# map(function, iterable) -> syntax
# ager map ma t elemt diye hai toh woh return bhi 5 hi krega
num = [1,2,3,4,5]

def double(n):
    return n + n

result = list(map(double,num))

print(result)

for i in result:
    # print('hello')
    print(i)

print(list(result)) # yha per resturn kr diya hai 


# _____________________________________________________________________________________________
#  Definition of map() in Python:
# The map() function in Python applies a given function to all the items in an iterable (like list, tuple, etc.) and returns an iterator (map object) containing the results.

# Syntax:
# map(function, iterable)


# Parameters:
# function → wo function jo iterable ke har element par apply hoga.
# iterable → list, tuple, ya koi bhi sequence jiske elements pe kaam karna hai.

# Return Type:
# map() returns a map object (iterator), jise list, tuple, ya loop ke through access karna padta hai.