
# last update 27.6.2021

import random


class Word:
    def __init__(self):
        self.word = random.choice(
            [i[:-1] for i in open('/Users/user/Desktop/GIT/Hangman/words.txt', 'r')])

    def __str__(self):
        return self.word

    def get_word(self):
        return self.word


def is_word_guessed(word, letters):
    s = str()
    for i in word:
        if i in letters:
            s += i
    return True if s == word else False


def get_guessed_word(word, letters):
    s = str()
    for i in word:
        if i in letters:
            s += f'{i} '
        else:
            s += '_ '
    return s


def get_available_letters(guessed):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = str()
    for i in letters.lower():
        if i not in guessed:
            s += i
    return s


def main():
    word = Word()
    # print(word)
    word = word.get_word()
    guesses = 8
    letters = str()
    while not is_word_guessed(word, letters) and guesses != 0:
        print('-'*40+f'\nYou have {guesses} guesses left')
        print(f'Available letters: {get_available_letters(letters)}')
        i = input('Guess a letter: ')
        if len(i) == 1:
            letters += i
        else:
            if is_word_guessed(word, i):
                print(get_guessed_word(word, i))
                break
            else:
                print(f'Sorry, bad guess. The word was {word}')
                break
        if i in word:
            print(
                f'Good guess : {get_guessed_word(word, letters)}')
        if i.upper() not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print(
                f'Nahh, that is not a letter: {get_guessed_word(word, letters)}')
            guesses -= 1
        else:
            print(
                f'Nahh, that latter is not in my word: {get_guessed_word(word, letters)}')
            guesses -= 1


if __name__ == '__main__':
    main()
