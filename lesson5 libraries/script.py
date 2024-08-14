#import random
from random import choice
from random import randint
from random import shuffle

import statistics
import sys
#from sys import argv
#from sys import exit

def main():
    print (flip_a_coin())
    print (randint(0,10))
    shuffle_list()
    avg()
    argv_print()


def flip_a_coin():
    #use this when importing whole module
    #return random.choice(["Heads","Tails"])
    return choice(["Heads","Tails"])

def get_an_int(a,b):
    return randint(a , b)

def shuffle_list():
    letters = ["A","B","C"]
    shuffle(letters)
    for letter in letters:
        print(letter)

def avg():
    print (statistics.mean([3,4,5,3,2,2,3,4]))

def argv_print():
    #try:
    #    print(f"Hello my name is {sys.argv[1]}")
    #except IndexError :
    #    print("Please provide a second argument")
    #variant
    if len(sys.argv) < 2:
        sys.exit ("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too  many arguments")
    #else:
    #    print(f"Hello my name is {sys.argv[1]}")
    print(f"Hello my name is {sys.argv[1]}")

def argv_print():
    if len(sys.argv) < 2:
        sys.exit ("Too few arguments")

    #arg[0] is program name, slice it [start:end]
    for arg in sys.argv[1:]:
        print(f"Hello my name is {arg}")


main()

