"декоратор"

# def aknazar(a):
#     def start():
#         print("Hello ")
#         a()
#         print("Bye")
#     return start


# @aknazar
# def add():
#     print(2 + 2)

# add()

# @aknazar
# def text():
#     print("qwertgyvfyuty tft tftftft ftfti tfyty")

# text()


"Множественное наследование"


# class Transport: # Родительский класс и Дочерний класс 
#     def __init__(self, marka, model, color):
#         "Атрибут объекта"
#         self.marka = marka
#         self.model = model
#         self.color = color
        
#     def info(self):
#         print(f"Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}") 

#     def __str__(self) -> str:
#         return f"Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}"


# class FuelCar(Transport):
#     def __init__(self, marka, model, color, fuel_tank):
#         Transport.__init__(self, marka, model, color)
#         self.fuel_tank = fuel_tank

#     def info(self):
#         print(f"Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}, бак - {self.fuel_tank}") 

#     def __str__(self):
#         return super().__str__() + " " + f"бак {self.fuel_tank} литров"

#     def drive(self):
#         print(f"Машина - {self.marka}-{self.model} едет на бензине")

# ae_86 = FuelCar("toyota", "ae-86", "white", 83)
# ae_86.info()
# print(ae_86)
# ae_86.drive()


# class ElectroCar(Transport):
#     def __init__(self, marka, model, color, battery):
#         Transport.__init__(self, marka, model, color)
#         self.battery = battery


#     def drive(self):
#         print(f"Машина - {self.marka}-{self.model} едет на электричестве")


# tesla = ElectroCar("tesla", "model-x", "Black", 100000)
# tesla.drive()


# class GybrydCar(ElectroCar, FuelCar):
#     def __init__(self, marka, model, color, battery, fuel_tank, speed):
#         ElectroCar.__init__(self, marka, model, color, battery)
#         FuelCar.__init__(self, marka, model, color, fuel_tank)
#         self.speed = speed
    
#     def drive(self):
#         if self.speed <= 60:
#             return ElectroCar.drive(self)
#         else:
#             return FuelCar.drive(self)


# toyota = GybrydCar("toyots", "prius", "Gray", 10000, 70, 80)
# toyota.drive()
# print(toyota.battery)
# print(toyota.fuel_tank)


"Магические методы"
"dunder методы -  (double underscore) методы с двойным подчеркиванием"


from typing import Any


class Math:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    
    def info(self):
        print(f"Первое число - {self.number_1} и второе {self.number_2}")

    def __str__(self): # print
        return f"Первое число - {self.number_1} и второе {self.number_2} это str"

    # def __repr__(self): # print
    #     return f"Первое число - {self.number_1} и второе {self.number_2} это repr"

    "Метод __call__ автоматически вызывается, когда к объекту обращаются как к функции"
    def __call__(self, a, b):
        print("Hello world")


    "Магические методы для арифметических действий"
    def __add__(self, other): # +
        return Math(self.number_1 + other.number_2, self.number_2)

    def __sub__(self, other): # -
        return Math(self.number_1 - other.number_2, self.number_2)

    def __mul__(self, other): # *
        return Math(self.number_1 * other.number_2, self.number_2)

    def __truediv__(self, other): # /
        return Math(self.number_1 / other.number_2, self.number_2)

    def __floordiv__(self): # //
        return Math(self.number_1 // self.number_2)

    
    "Магические методы для операторов сравнения"
    def __gt__(self, other): # >
        return self.number_1 > other.number_1


math = Math(12, 12)
math_2 = Math(2, 5)


# math.info()
# print(math) # str, repr

# math(12, 12) # call


"Магические методы для арифметических действий"

# print(math + math_2)
# print(math - math_2)
# print(math * math_2)
# print(math / math_2)
# print(math // math_2)



"Магические методы для операторов сравнения"

print(math > math_2)
