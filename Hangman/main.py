
# last update 21.6.2021

import random


class Word:
    def __init__(self):
        self.word = random.choice(
            [i[:-1] for i in open('/Users/user/Desktop/GIT/Hangman/words.txt', 'r')])

    def __str__(self):
        return self.word


def main():
    word = Word()
    print(word)


if __name__ == '__main__':
    main()
