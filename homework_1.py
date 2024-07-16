                        # 1 задание:

# class Fruits():
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def info(self):
#         print(f"{self.name} цвета {self.color}, весит {self.weight}гр")

# apple = Fruits("Яблоко", "красный", 175)
# apple.info()

# banana = Fruits("Банан", "желтый", 134)
# banana.info()

# orange = Fruits("Апельсин", "оранжевый", 153)
# orange.info()

                        # 2 задание:

# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def check_pages(self):
#         if self.pages < 100:
#             print(f"Книга {self.title} автора {self.author} является тонкой книжкой")
#         elif 100 < self.pages < 300:
#             print(f"Книга {self.title} автора {self.author} является средней книжкой")
#         elif self.pages > 300:
#             print(f"Книга {self.title} автора {self.author} является толстой книжкой")
#         else:
#             print("Ошибка")

# geometry = Book("геометрия", "А.Б.Погорелов", 90)
# geometry.check_pages()

# To_Kill_a_Mockingbird = Book("убить пересмешника", "Харпер Ли", 412)
# To_Kill_a_Mockingbird.check_pages()

# Fight_Club = Book("бойцовский клуб", "Паланик Чак", 256)
# Fight_Club.check_pages()



                        # Доп. задание:

# class Car: 
#     def __init__(self, marka, model, color):
#         self.marka = marka
#         self.model = model
#         self.color = color
#         self.is_start = False 
#         self.bak = 0
        
#     def info(self):
#         print(f"Марка машины:{self.marka}, модель:{self.model}, цвет:{self.color}") 
        
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True 
#             print(f"машинa {self.marka} - {self.model} заведена")
#         else:
#             print(f"В машине {self.marka} - {self.model} нет топлива")
            
    
#     def stop(self):
#         self.is_start = False 
#         print(f"машинa {self.marka} - {self.model} заглушена")
        
        
#     def drive(self, city):
#         if self.is_start == True:
#             print(f"машинa {self.marka} - {self.model} едет в {city}")
#         else:
#             print(f"Машина {self.marka} - {self.model} не заведена!")
        

#     def energy(self, city):
#         print(f"Машина {self.marka} - {self.model} едет в {city}, чтобы пополнить бак")
#         self.bak = 100
        


# merс = Car("merсedes", "cls", "black") 
# merс.info()
# merс.energy("Osh")
# merс.start()
# merс.drive("Bishkek")
# merс.stop()



