import random
import time
from colorama import Fore


class Revolver:
    def __init__(self, cylinder = [0, 0, 0, 1, 0, 0]):
        self.cylinder = cylinder  
        self.spin_chamber()

    def spin_chamber(self):
        random.shuffle(self.cylinder)  

    def shoot(self):
        chekatel = self.cylinder.pop(0)  
        if chekatel == 1:
            return True  
        else:
            return False 

class Player:
    def __init__(self, is_alive = True):
        self.is_alive = is_alive

    def take_shot(self, revolver):
        print(Fore.YELLOW)
        input("\nНажмите Enter, чтобы сделать выстрел...")
        print("Вы заряжаете револьвер и нажимаете на курок...")
        time.sleep(2)
        print()
        if revolver.shoot():
            print(Fore.LIGHTRED_EX + "Пуля выстрелила! Вы проиграли...")
            self.is_alive = False
        else:
            print(Fore.LIGHTGREEN_EX + "Фух, пуля оказалась холостой. Вы выжили!")



def game():
    six_pistols = Revolver()
    John_Wick = Player()

    while John_Wick.is_alive:
        John_Wick.take_shot(six_pistols)
        if John_Wick.is_alive:
            choice = input(Fore.WHITE + f"\nХотите продолжить игру? (да/нет): ")
            if choice != 'да':
                break
            else:
                six_pistols.spin_chamber()  

    if John_Wick.is_alive:
        print(Fore.LIGHTGREEN_EX + "Вы решили остановиться. Надеюсь вы проверили свою удачу в этой игре!")
    else:
        print(Fore.LIGHTRED_EX + "К сожалению, вам не повезло. Вы проиграли.")


print(Fore.RED + "\nДобро пожаловать в игру <Русская рулетка>. Правила этой игры очень просты: \nВы берёте револьвер в котором всеволишь одна настоящая пуля. \nВаша задача - выстрелить себе в голову и тем самым проверить свою удачу. \nЖелаю приятной игры!")


while True:
    start = input(Fore.LIGHTCYAN_EX + "Вы хотите начать игру? Да/Нет: ")
    if start == "Да":
        game()
        break
    elif start == "Нет":
        print("Ладно.")
        break
    else:
        print("Ошибка!")
        continue