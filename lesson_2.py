# class Car:
#     def __init__(self, model, color):
#         self.model = model 
#         self.color = color 

#     def info(self):
#         print(f"model: {self.model}, color: {self.color}")
    

# mers = Car("mersedes - cls", "black")
# bmw = Car("BMW - m5 f90", "blue")
# mers.info()
# bmw.info()
# print()

# class Mersedes(Car):
#     def __init__(self, model, color, is_jump):
#         # super().__init__(model, color)
#         Car.__init__(self, model, color)
#         self.is_jump = is_jump

#     def info(self):
#         print(f"model: {self.model}, \ncolor: {self.color}, \nis_jump: {self.is_jump}")
#     def is_jump(self):
#         print(f"У машины {self.model}, есть система <<самовытаскивания>>")

# mers1 = Mersedes("Mersedes e500", "Grey")
# mers1.info()
# mers1.is_jump()


# from abc import ABC, abstractmethod

# # Абстрактный класс
# class Payment(ABC):
#     @abstractmethod
#     def proccess_payment(self, amount):
#         pass

# # Класс для обработки платежей 
# class CreditCardPayment(Payment):
#     def proccess_payment(self, amount):
#         return print(f"Обработка по кредитной карте, на сумму {amount}$")

# # Класс для обработки платежей
# class PayPalPayment(Payment):
#     def proccess_payment(self, amount):
#         return print(f"Обработка по PayPal, на сумму {amount}$")
    
# def make_payment(payment_method, amount):
#     payment_method.proccess_payment(amount)

# credits = CreditCardPayment()
# paypal = PayPalPayment()

# make_payment(credits, 100)
# make_payment(paypal, 200)



# "Наследование и абстракция"
# " DRY - Don`t Repeat Yourself == не повторяй себя"


# class Transport: # Родительский класс и Дочерний класс 
#     def __init__(self, marka, model, color):
#         "Атрибут объекта"
#         self.marka = marka
#         self.model = model
#         self.color = color
        
#     def info(self):
#         print(f"Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}") 


# class Car(Transport): # Родительский класс
#     pass

# # bmw = Car("bmw", "m5 - f90", "black") 
# # bmw.info()


# class Mersedes(Car): # Дочерний класс
#     def __init__(self, marka, model, color, is_jump):
#         # super().__init__(marka, model, color)
#         Car.__init__(self, marka, model, color)
#         self.is_jump = is_jump

#     def info(self):
#         print(f"Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}, is jump? {self.is_jump}") 


# # merс = Mersedes("merсedes", "cls", "black", False) 
# # merс.info()


# class Animal:

#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self):
#         print("MEOW-MEOW")


# class Dog(Animal):
#     def make_sound(self):
#         print("GAF-GAF")


# class Cow(Animal):
#     def make_sound(self):
#         print("Moo-Moo")

# # cat = Cat()
# # dog = Dog()
# # cow = Cow()


# # cat.make_sound()
# # dog.make_sound()
# # cow.make_sound()



# def make_sound():
#     print("Moo-Moo")

# def make_sound():
#     print("MEOW")

# def make_sound():
#     print("GAF")


# make_sound()
# make_sound()
# make_sound()

# number = 5
# print(number) 
# number = 7



