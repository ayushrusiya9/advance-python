# Iterator ek aisa object hota hai jo ek time par ek hi value deta hai jab hum uspar next() function use karte hain.
# Python me koi bhi object agar ye dono method rakhta hai:
# __iter__()
# __next__()
# toh wo iterator kehlata hai.

# Generato definition:
# A Generator in Python is a special type of iterator that is used to produce a sequence of values lazily, that is, one value at a time, instead of storing all the values in memory.

# It is created using a function that contains the yield keyword, or using a generator expression.
# Each time the generator’s __next__() method is called, the function resumes execution from where it last yielded a value, until it raises StopIteration.

def Gen(n):
    for i in n:
        yield i

l = [1,2,3,4,5]

func = Gen(l)

print(next(func)) 
print('hello  world!') 
print(next(func))
print(next(func))
print(next(func))
print(next(func))

# my learning:
# Generator ek iterator hi hota hai, lekin usse likhna aur use karna bahut easy hota hai  aur ye data ko memory efficient way me generate karta hai.