
" ООП - Объектно Ориентрованное Программирование "

"Змеиный регистр"
full_name = "Abdykadyrov"
snake_case = True

"Верблюжий регистр"
FullName = "Abdykadyrov"
SuperCar = "test"
CamekCase = True


class Car: # шаблон или же чертеж
    "Атрибут класса"
    # marka = "merсedes"
    # model = "cls"
    # color = "black"

    "__init__ - конструктор"
    " self - ссылка на текущий объект (сам объект)"
    def __init__(self, marka, model, color):
        "Атрибут объекта"
        self.marka = marka
        self.model = model
        self.color = color
        self.is_start = False 
        self.bak = 10 
        
    def info(self):
        print(f"Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}") 
        
    def start(self):
        if self.bak > 0:
            self.is_start = True 
            print(f"машинa {self.marka} - {self.model} заведена")
        else:
            print(f"В машине {self.marka} - {self.model} нет топлива")
    
    def stop(self):
        self.is_start = False 
        print(f"машинa {self.marka} - {self.model} заглушена")
        
        
    def drive(self, city):
        if self.is_start == True:
            print(f"машинa -{self.marka} - {self.model} едет в {city}")
        else:
            print(f"Машина {self.marka} - {self.model} не заведена!")

merс = Car("merсedes", "cls", "black") 
merс.info()

merс.start()
merс.drive("Osh")
merс.stop()
# merс.drive()
# print(merс.marka, merс.model, merс.color) 


bmw = Car("bmw", "jt", "white")
bmw.info()
# print(bmw.marka, bmw.model, bmw.color)

