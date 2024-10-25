'''Import random module to implement random.choice() function'''
import random
from climage import convert


def random_line(text):
    '''Opens and reads lines of a UTF-8 encoded file, returning a random line'''
    with open(text, 'r', encoding='UTF-8') as file:
        line = file.readlines()
        return random.choice(line)


def main():
    '''Prints random line from facts.txt; verify your path'''
    print(random_line('facts.txt'))
    '''Take in PNG and output as ANSI to terminal'''
    output = convert('linky.png', is_unicode=True)
    print(output)


if __name__ == "__main__":
    main()


