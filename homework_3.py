# class Computer:
#     def __init__(self, name, cpu, memory):
#         self.name = name
#         self.__cpu = cpu
#         self.__memory = memory
    
#     @property
#     def cpu(self):
#         return self.__cpu
    
#     @property
#     def memory(self):
#         return self.__memory
    

#     def __make_computations(self):
#         print(f"""Результат сложения: {self.cpu+self.memory},\nРезультат вычитания: {self.cpu-self.memory},\nРезультат умножения: {self.cpu*self.memory},\nРезультат деления: {self.cpu/self.memory}""")
        

#     @property
#     def make_computions(self):
#         return self.__make_computations


# computer = Computer("Intel Core i5", 12600, 8)
# computer.make_computions()

# class Laptop(Computer):
#     def __init__(self, name, cpu, memory, memory_card):
#         Computer.__init__(self, name, cpu, memory)
#         self.__memory_card = memory_card

#     @property
#     def memory_card(self):
#         return self.__memory_card
    
#     def info(self):
#         print(f"Процессор: {self.cpu}, память: {self.memory}, карта памяти: {self.memory_card}")
# print()
# laptop = Laptop("Intel Core i7", 11800, 16, 755)
# laptop.make_computions()
# laptop.info()



