def multiply(num):
    return num**2
a = [1,2,3,4,5]
b = list(map(multiply,a))
print(b)
txt = str(input())
lower = upper = 0
for i in txt:
    if i.islower():
        lower+=1
    else:
        upper+=1
print(f"Lower: {lower}")
print(f"Upper: {upper}")
def Palin():
    s = str(input())
    m = txt[::-1]
    if m==s:
        return True
    return False
list = []
s = str(input())
for i in s:
    list.append(i)
list_reversed = reversed(list)
m = ''.join(list_reversed)
if m==s:
    print("True")
else:
    print("False")
import time
n = int(input())
m = int(input())
time.sleep(m/1000)
print(n**0.5)
def check_tuple(items):
    result = all(items)
    print(result)
tuple1 = tuple(map(int, input().split()))
check_tuple(tuple1)
