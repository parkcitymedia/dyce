#!/bin/python3
from random import randint
cointoss = ["heads", "tails"] #pre-define coin sides
print("Dyce Roller CLI Mini-Script 0.0.02")
def rollprompt():
	try:
		sides = int(input("number of sides on die: "))
	except(ValueError):
		print("not a proper number! please type an integer using characters 0-9 only!")
		print(" ")
		print("new roll ---")
		rollprompt()
	roll(sides)
def roll(sides):
	if sides < 0:
		print("you can't roll negatives, give me a break.")
		print(" ")
		print("new roll ---")
		rollprompt()
	if sides == 0:
		print("well it's obviously ONLY going to be 0. n\that's litterally nothing")
		print(" ")
		print("new roll ---")
		rollprompt()
	if sides == 1:
		print("well it's obviously ONLY going to be 1. n\that's not fair, nor is it physically possible")
		print(" ")
		print("new roll ---")
		rollprompt()
	if sides == 2:
		print("flipped a coin; landed on: ")
		print(cointoss[randint(0, 1)])
		print(" ")
		print("new roll ---")
		rollprompt()
	if sides == 69: #nice
		print("HAHA NICE")
		print("but seriously - ")
		print("rolled a D69, which landed on: ") #nice
		print(randint(1, 69)) # nice
		print(" ")
		print("new roll ---")
		rollprompt()
	if sides == 100:
		print("rolled a percentile die, which landed on: ")
		print(str(randint(1, 100)) + "%")
		print(" ")
		print("new roll ---")
		rollprompt()
	if sides > 100:
		print("rolled a thicc D" + str(sides), ", which landed on: ")
		print(randint(1, sides))
		print(" ")
		print("new roll ---")
		rollprompt()
	elif sides >= 3:
		print("rolled a D" + str(sides), ", which landed on: ")
		print(randint(1, sides))
		print(" ")
		print("new roll ---")
		rollprompt()
rollprompt()
