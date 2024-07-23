import random
from game import HangmanGame
from words import word_list 
from termcolor import cprint

def main():
    word = random.choice(word_list)
    game = HangmanGame(word)
    
    cprint("Добро пожаловать в игру <Угадай слово>", color="light_magenta", attrs=['bold'])
    game.display()
    
    while not game.is_game_over():
        guess = input("\nПожалуйста, введите букву или слово: ")
        if len(guess) == 1:
            game.guess_letter(guess)
        else:
            game.guess_word(guess)
        
        game.display()
    
    if "_" not in game.word_completion:
        cprint("Поздравляю! Вы отгадали слово! Вы выиграли!", color="light_green")
    else:
        cprint("Ой, к сожалению у вас закончились попытки. Отгаданное слово: " + game.get_hidden_word() + ". Повезет в следующий раз!", color="light_red")


if __name__ == "__main__":
    main()