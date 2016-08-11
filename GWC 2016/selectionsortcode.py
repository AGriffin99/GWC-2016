import random

which_quote = random.randint(0, 10)
print(which_quote)
if which_quote < 3:
	print("'tis merely a flesh wound")
elif which_quote < 5:
	print("we are the knights who say ni")
elif which_quote < 8:
	print("an african swallow or a european swallow?")
else:
	print("bravely brave Sir Robin ran away")
