#  decorater means function ke ander function uske ander function repeat krte hai
# Decorator = Function that modifies behavior of another function.
# definition:- A decorator is a function that takes another function as an argument, adds some extra functionality to it, and returns a new function — without modifying the original function’s code.

import time


def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__name__} is run in {end - start} time.')
        return result
    return wrapper


@timer
def example_function(n):
    time.sleep(n)


example_function(2)