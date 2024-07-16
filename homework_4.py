#                     Основная задание:

# class MagicCalculator:
#     def __init__(self, number_1, number_2):
#         self.number_1 = number_1
#         self.number_2 = number_2

#     def __add__(self, other): 
#         return f"Сумма: {self.number_1 + other.number_1, self.number_2 + other.number_2}"

#     def __sub__(self, other): 
#         return f"Разность: {self.number_1 - other.number_1, self.number_2 - other.number_2}"

#     def __mul__(self, other): 
#         return f"Произдведение: {self.number_1 * other.number_1, self.number_2 * other.number_2}"

#     def __truediv__(self, other): 
#         if other.number_1 == 0 or other.number_2 == 0:
#             raise ZeroDivisionError("На ноль делить нелья!")
#         return f"Частная с остатом: {self.number_1 / other.number_1, self.number_2 / other.number_2}"

#     def __floordiv__(self, other): 
#         if other.number_1 == 0 or other.number_2 == 0:
#             raise ZeroDivisionError("На ноль делить нелья!")
#         return f"Частная без осткатка: {self.number_1 // other.number_1, self.number_2 // other.number_2}"
    

# legendary_numbers = MagicCalculator(290, 10)
# genius_numbers = MagicCalculator(10, 290)
# print(f"Результат - {legendary_numbers // genius_numbers}")



                        # Доп. задание:

# class Book:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
    
#     def __lt__(self, other):
#         return self.year < other.year
    
#     def __le__(self, other):
#         return self.year <= other.year

#     def __gt__(self, other):
#         return self.year > other.year
    
#     def __ge__(self, other):
#         return self.year >= other.year
    
#     def __eq__(self, other):
#         return self.year == other.year
    
#     def __ne__(self, other):
#         return self.year != other.year

#     def __str__(self):
#         return f"Название: {self.name}\nАвтор: {self.author}\nГод издания: {self.year}\n"
    
# book_1 = Book("Бойцовский клуб", "Чак Паланик", 1996)
# book_2 = Book("Убить пересмешника", "Харпел Ли", 1960)
# print(book_1)
# print(book_2)
# print(book_1 > book_2)





