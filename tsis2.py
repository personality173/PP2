#LIST exercises:
#1-exercise
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#2-exercise
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#3-exercise
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#4-exercise
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#5-exercise
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#6-exercise
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#7-exercise
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#8-exercise
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#TUPLE exercises:
#1-exercise
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#2-exercise
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#3-exercise
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#4-exercise
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#SETS exercises:
#1-exercise
fruits = ("apple", "banana", "cherry")
if "apple" in fruits:
    print("Yes, apple is a fruit!")
#2-exercise
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#3-exercise
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#4-exercise
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#5-exercise
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#Dictionary exercises:
#1-exercise
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))
#2-exercise
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964

}

car["year"] = 2020
#3-exercise
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964

}
car["color"] = "red"
#4-exercise
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#5-exercise
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear(

#WHILE exercises:
#1-exercise
i = 1
while i < 6:
  print(i)
  i +=1
#2-exercise
i = 1
while i < 6:
    if i == 3:
        break
    i += 1
#3-exercise
i = 0
while i < 6:
    if i == 3:
        continue
    print(i)
#4-exercise
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#LOOPS exercises:
#1-exercise
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#2-exercise
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
#3-exercise
for x in range(6):
    print(x)
#4-exercise
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
