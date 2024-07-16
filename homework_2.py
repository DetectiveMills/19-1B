class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Fullname: {self.fullname}")
        print(f"Age: {self.age}")
        print(f"Marital status: {'Married' if self.is_married else 'Single'}")


class Teacher(Person):
    salary = 0  

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        self.salary = 30000 
        for i in range(self.experience // 3):
            self.salary += 3000 
        print(self.salary)

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Опыт работы: {self.experience} год")
        print(f"Зарплата: ${self.salary}")



teacher1 = Teacher("Кутя", 15, False, 9)
teacher1.calculate_salary()
teacher1.introduce_myself()
