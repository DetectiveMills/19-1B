# from test import sum as plus, sub, mult
# from package.test import sub
"from <Название модуля> import <что мы хотим импортировать>"

# plus(3,3)
# sub(3,3)
# mult(3,3)
# print(sum([12,1212,12]))

# from test import sum as plus

# plus(3,3)


# from test import * # из модуля все содержимое

# sum(2,2)
# sub(4,4)


# import package.test as test 

# from package import test

# test.sub(3,2)


"""Декомпозиция -- разделение кода по модулям"""


"Кастомные модули: lesson_1, start, test "


"Встроенные (вложенные) модули: random, time, datetime, math, os"

"random"

# import random

# massiv = ["12", 12, 12345, "qwerty"]
# random_choice = random.choice(massiv)
# # random_massiv = random.shuffle(massiv)
# random.shuffle(massiv)
# lucky_num = random.randint(1,10)
# print(lucky_num)
# print(random_choice)
# print(massiv)


# "time"
# import time
# # from time import sleep # vтак не советуется

# print("Hi")
# time.sleep(2)
# # sleep(2) 
# print("Bye")

"Внешние модули: colorama , termcolor, aiogram, django"

from termcolor import cprint

print("Hello world")
cprint("Hello world", color="light_green", on_color="on_red", attrs=["bold"])

"MacOs, linux"
"source venv/bin/activate"
"deactivate"
"Win"
"./venv/Scripts/activate"
"deactivate"