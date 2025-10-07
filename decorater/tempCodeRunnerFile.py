

def cache(func):
    print('hello')
    def wrapper(*args):

        args = tuple(arg + 5 for arg in args)
        
        result = func(*args)

        return result
    return wrapper

@cache
def long_running_function(a, b):
    
    return a + b



print(long_running_function(3,3))
print(long_running_function(8,3))
print('line number 23')
print(long_running_function(1,3))