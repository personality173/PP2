#1-exercise
def gen(n):
    for i in range(n):
        yield i**2
n = int(input())
for i in gen(n):
    print(i)
#2-exercise
def gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
n = int(input())
lst = []
for i in gen(n):
    lst.append(i)
print(lst)
#3-exercise
def gen(n):
    for i in range(0, n):
        if i % 3 == 0 or i % 4 == 0:
            yield i
n = int(input())
for i in gen(n):
    print(i)
#4-exercise
def squares(a, b):
    for i in range (a, b):
        yield i**2
a = int(input())
b = int(input())
for i in squares(a, b):
    print(i)
#5-exercise
def gen(n):
        while n >= 0:
            yield n
            n -= 1
n = int(input())
for i in gen(n):
    print(i)