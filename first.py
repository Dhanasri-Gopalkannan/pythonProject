'''l1=[(i,j) for i in range(3) for j in range(i)]
print(l1)'''

'''l=[2,4,6,8,9]
l2=[i for i in l if l % 2 == 0]
print(l2)#error'''

'''numbers=[i*10 for i in range(1,6)]
print(numbers)'''

'''s = "we are doing revision in python concepts"
print(s.startswith("we"))
print(s.endswith("cepts"))'''

'''s = "Learning python is very very easy"
print(s.count("a"))'''

'''s1 = "CONVERT UPPER CASE TO lower case"
print(s1.lower())
s2 = "convert lower case to UPPERCASE"
print(s2.upper())
s3 = "eaach word first letter should be CAPITAL"
print(s3.title())
s4 = "only the FIRST character of the string should be capital"
print(s4.capitalize())
s5 = "convert UPPER TO lower"
print(s5.swapcase())'''

'''print(4 | 8)
print(4 & 8)

print(6 ^13)'''


'''print(int(10.0))
print(int(True))
print(int("24"))
print(int(2+4j))'''

'''print(float(20))
print(float(True))
print(float("34"))
print(float(2+4j))'''
'''print(bool(-1))
print(bool(0.26))
print(bool(""))'''

'''def even(n):
    if n % 2 == 0:
        return True
    else:
        return False
l = [12,13,14,15,16]
l1 = list(filter(even, l))
print(l1)'''

'''def fetch(s):
    for i in s:
        if i.isdigit():
            return True
        else:
            return False
data = "dhana221099"
l1 = list(filter(fetch,data))
print(l1)'''

'''city = "Hydrabad"
for i in city[:6:1]:
    print(i)'''

'''l1 = [10,20,30,33,54]
l2 = [2,4,6,8]
for i in l1:
    print(l1)
for j in l2:
    if j%3 == 0:
        break
    else:
        print(j)'''

'''l2 = lambda x,y,z : x%3 != 0 and y+z
print(l2(10,20,30))'''

'''l = lambda  x,y : x>y and x<y
print(l(10,20))'''

'''def wish(a,b):
    print(a+b)
    print("welcome")
a = wish(10,20)
print(a)'''

'''def cube(y):
    return y*y*y
    print("hello")

g = lambda x: print(x*x*x)
print(g(4))
print(cube(3))'''

'''def myfunc(n):
    return lambda a:a*n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))'''

'''t = (10,-4,62,-5,100,0,1)
def calculate(num):
    if num!=62:
        return num
    else:
        pass

t = tuple(filter(calculate,t))
print(t)'''

'''s = "VisHAkaPatnam"
def verify(n):
    if n.islower():
        return n
    else:
        pass

s = set(list(filter(verify,s)))
print(s)'''

'''t = (10,20,30,40,11)
print(list(map(lambda a:a%2 == 0, t)))'''

'''def collect(a,*b):
    print(a,b)

collect(12,34,"python","variable")

while True:
    print("hi")

while False:
    print("hello")

for i in range(20,10,-1):
    print(i)

for i in range(10):
    if i==5:
        continue
    else:
        print(i)

l = lambda a,b,c:a+b+c
print(l(3,7,9))

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

l=[12,13,14,15,16,17,19]
l1 = list(filter(even,l))
print(l1)

l=[11,12,13,14,15,16,17]
l1 = list(filter(lambda n:n%2 == 0,l))
print(l1)

l=[2,3,4,5,6]
l1 = list(map(lambda a:a**3,l))
print(l1)

from main import a
print(a)
print(__name__)

from math import *
print(sqrt(2))
print(ceil(2.4))
print(floor(5.6))
print(fabs(12.785))
print(log(12))
print(sin(2))
print(tan(3))'''

'''from random import *

#print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep=(''))

data = "0123456789 a-z A-Z @#*!"
n = int(input("enter the length of the password:"))
for i in range(n):
    print(choice(data))'''

