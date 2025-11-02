import sys

a = 10
s = "ayush"
com = 10 + 1j
f = 2.12
l = [1,'ayus',2,3]
t = (1,2,'ayush',4)
se = {1,2,3,4}
d = {'1':1,'2':2}

# print(sys.getsizeof(a))
# print(sys.getsizeof(s))
# print(sys.getsizeof(com))
# print(sys.getsizeof(f))
# print(sys.getsizeof(l))
# print(sys.getsizeof(t))
# print(sys.getsizeof(se))
# print(sys.getsizeof(d))

forl = [1,2,3]
fort = (1,2,3)
print('list size :',sys.getsizeof(forl),'\n' 'tuple size :',sys.getsizeof(fort))