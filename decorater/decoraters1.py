

def debug(func):
    def wrapper(*args,**kwargs):
        args_values = ', '.join(str(arg) for arg in args)
        kwargs_values = ', '.join(f'{k} = {v}' for k, v in kwargs.items())
        result = func(*args, **kwargs)
        print(f'{func.__name__} {args_values} and {kwargs_values}')
        return result
    return wrapper

@debug
def hello():
    print('hii')

hello()

@debug
def greet(name,greeting='welcome!'):
    print(f'{greeting}, {name}')

greet('ayush',greeting='apka swagat hai ')