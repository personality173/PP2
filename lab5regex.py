import re
#1-exercise
s = input()
result = re.search(r'ab*?', s)
print(result)
#2-exercise
s = input()
result = re.search(r'ab{2,3}?', s)
print(result)
#3-exercise
s = input()
result = re.search(r'^[a-z]+_[a-z]+$', s)
print(result)
#4-exercise
s = input()
result = re.search(r'[A-Z]{1}[a-z]+', s)
print(result)
#5-exercise
s = input()
result = re.search(r'a.*?b$', s)
print(result)
#6-exercise
s = input()
result = re.sub(r"[ ,.]", ":", s)
print(result)
#7-exercise
s = input()
result = re.findall(r'(.*?)_([a-zA-Z])',s)
print(result)
#8-exercise
list = []
s = input()
camel = re.split('_', s)
for i in camel:
    list.append(i.capitalize())
    camel_case = "".join(list)
print(camel_case)
#9-exercise
s = input()
words = re.findall('.[^A-Z]*', s)
result = ' '.join(words)
print(result)
#10-exercise
s = str(input())
result = re.findall('[A-Z][a-z]*', s)
for i in result:
     x = i.lower()
     print(x, end="_")
