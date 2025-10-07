# The reduce() function applies a given function to all elements in an iterable one by one, reducing them to a single calculated value.

# from functools import reduce
# reduce(function, iterable)


from functools import reduce #  2nd way
# import functools # first way to access reduce

num = [1,2,3,4,5,6,7,8,9,10]

def sum(x,y):
    return x + y

result = reduce(sum,num) # 2nd way
# result = functools.reduce(sum,num) # 1st way 

print(result)