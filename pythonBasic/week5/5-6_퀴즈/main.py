import random

print("5-6 - 퀴즈\n")

from random import *

participants = [i for i in range(1, 21)]
# participants = range(1, 21)
# participants = list(participants)

# while len(winner) < 4:
#     shuffle(participants)
#     winner.add(choice(participants))

winner = sample(participants, 4)
record = winner.copy()
shuffle(winner)

chicken = choice(winner)
winner.remove(chicken)
coffee = winner

print("** congratulation **")
print(f"winner {record}")
print(f"chicken : {chicken}")
print(f"coffee : {coffee}")
