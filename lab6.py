

import os

#1-exercise
# print(os.listdir())

#2-exercise

# print(os.access('C:\\Users\\Ернур\\PycharmProjects\\pythonProject\\test', os.F_OK))
# print(os.access('C:\\Users\\Ернур\\PycharmProjects\\pythonProject\\test', os.R_OK))
# print(os.access('C:\\Users\\Ернур\\PycharmProjects\\pythonProject\\test', os.W_OK))
# print(os.access('C:\\Users\\Ернур\\PycharmProjects\\pythonProject\\test', os.X_OK))

#3-exercise
# print(os.path.exists('C:\\Users\\Ернур\\PycharmProjects\\pythonProject\\test\\ernur')) #when the given path does not exist
# print(os.path.basename('C:\\Users\\Ернур\\PycharmProjects\\pythonProject\\test')) # the last name of file
# print(os.path.dirname('C:\\Users\\Ернур\\PycharmProjects\\pythonProject\\test')) # the directory before the last filename

#4-exercise
# with open('words.txt', 'r') as f:
#     line_count = 0
#     for line in f:
#         line_count += 1
# print(line_count)

#5-exercise
# my_list = [input()]
# file_path = 'words.txt'
#
# with open(file_path, 'w') as f:
#     for item in my_list:
#         f.write(f'{item}\n')

#6-exercise
# import string, os
# if not os.path.exists("letters"):
#    os.makedirs("letters")
# for letter in string.ascii_uppercase:
#    with open(letter + ".txt", "w") as f:
#        f.writelines(letter)

#7-exercise
# import shutil
# shutil.copy('words.txt', 'words1.txt')

#8-exercise
# print(os.access('C:\\Users\\Ернур\\PycharmProjects\\pythonProject\\test1', os.F_OK))
# print(os.path.exists('C:\\Users\\Ернур\\PycharmProjects\\pythonProject\\test1'))
# os.rmdir('C:\\Users\\Ернур\\PycharmProjects\\pythonProject\\test1')