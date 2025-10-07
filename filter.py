# The filter() function is used to filter out elements from an iterable for which a given function returns True.
# filter(function,itrable(list/tuple))

num = (1,2,3,4,5,6,7,8,9,10)

def even(n):
    return n % 2 == 0

result = filter(even,num)

print(result)

for i in result:
    print(i)

print(list(result))