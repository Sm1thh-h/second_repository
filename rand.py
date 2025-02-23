# # import random

# # number = random.randint(1, 10)
# # print(number)

# #printing cards at random


# import random

# cards = ["Jack", "Queen", "King", "spade", "pyramid"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

# import statistics

# a = [30, 40]

# print(statistics.mean(a))

import sys

if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello, my name is", sys.argv[1])


#this is a better looking code, checking for error and printing the result


import sys


# check for errors

if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")

print("hello, my name is", sys.argv[1])