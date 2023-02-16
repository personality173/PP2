
#Creating Comment
# - the symbol of comment
print("Hello, Alem!")
print("Hello, World!") #This is a comment
#Multiline Comments
#This is a comment
#written in
#more than just one line
print("Hello, World!")
if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")
#VARIABLES:
x = 5
y = "Hello, World!"
print(x)
print(y)
x = 10      # x is of type int
x = "Saken" # x is now of type str
print(x)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
x = 5
y = "John"
print(type(x)) - the output <class 'int'>
print(type(y)) - the output <class 'str'>
x = "John"
# is the same as
x = 'John'
a = 4
#is not the same
A = "Sally"
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#Illegal variable names:
#we can not write like this because we have to write the variable names without '-', probels and start with numbers
2myvar = "John"
my-var = "John"
my var = "John"
#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #the output is "Python is awesome"
x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #the output is also "Python is awesome"
x = 7
y = 11
print(x + y) #the output is 18
x = 5
y = "John"
print(x, y) # the output is 5 John
#Global Variables
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc() #the output is "Python is awesome"
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc() #the output is "Python is fantastic"
print("Python is " + x) # the output is "Python is awesome"
#The global Keyword
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) #the output is "Python is fantastic"
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) #the output is "Python is fantastic"
#Setting the Data Type
x = "Hello World"	str
x = 20	int
x = 20.5	float
x = 1j	complex
x = ["apple", "banana", "cherry"]	list
x = ("apple", "banana", "cherry")	tuple
x = range(6)	range
x = {"name" : "John", "age" : 36}	dict
x = {"apple", "banana", "cherry"}	set
x = frozenset({"apple", "banana", "cherry"})	frozenset
x = True	bool
x = b"Hello"	bytes
x = bytearray(5)	bytearray
x = memoryview(bytes(5))	memoryview
x = None	NoneType
#Python Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
#Random Number
import random
print(random.randrange(1, 10))
#Python Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
#Python Strings
print("Hello")
print('Hello')
a = "Hello"
print(a)
a = """
Lorem
ipsum
dolor
sit
amet,
consectetur
adipiscing
elit,
sed
do
eiusmod
tempor
incididunt
ut
labore
et
dolore
magna
aliqua.
"""
print(a)
a = "Hello, World!"
print(a[1]) #the output is "e"
for x in "banana":
  print(x) # b a n a n a

a = "Hello, World!"
print(len(a)) # the output is 13
txt = "The best things in life are free!"
print("free" in txt) # the output is True
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt) # the output is true because it does not have expensive in txt
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Python - Slicing Strings
b = "Hello, World!"
print(b[2:5]) #output "llo"
b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[2:])
b = "Hello, World!"
print(b[-5:-2]) # output is "orl"
#Python - Modify Strings
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(a.replace("H", "J")) #the output is "Jello, World!"
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
a = "Hello"
b = "World"
c = a + b
print(c) #the output "HelloWorld"
a = "Hello"
b = "World"
c = a + " " + b
print(c) #the output "Hello World"
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #My name is John, and I am 36
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #I want 3 pieces of item 567 for 49.95 dollars.
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) #I want to pay 49.95 dollars for 3 pieces of item 567
txt = "We are the so-called \"Vikings\" from the north."
#Python Booleans
print(10 > 9) True
print(10 == 9) False
print(10 < 9) False
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print(bool("Hello")) #True
print(bool(15)) #True
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
bool(False) #False
bool(None) #False
bool(0) #False
bool("") #False
bool(()) #False
bool([]) #False
bool({}) #False
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj)) #the output False
def myFunction() :
  return True
print(myFunction()) #True
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!") # "Yes"

x = 200
print(isinstance(x, int))
#Python If ... Else
a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

if a > b: print("a is greater than b")
a = 2
b = 330
print("A") if a > b else print("B")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") #Above ten,
and also above 20!
username = input("Enter username:")
print("Username is: " + username)
#Python String Formatting
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
txt = "The price is {:.2f} dollars" #the output The price is 49.00
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
