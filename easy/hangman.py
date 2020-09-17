import random

print("H A N G M A N")
words = ["program", "python", "apple", "orange", "monkey"]

if(input("Type \"play\" to play the game, \"exit\" to quit: ") == "play"):
	life = 7
	tries_letters = []
	word = random.choice(words)
	print(word)
	hide_word = "-" * len(word)
	print(hide_word)

	while(True):
		print("Life: " + str(life) + "\n" + hide_word)
		letter = input("Input letter: ")
		if(letter in tries_letters):
			print("You already typed this letter")
			continue
		if(letter in word):
			#hide_word[word.index(letter)] = letter
			hide_word = hide_word[:word.index(letter)] + letter + hide_word[word.index(letter)+1:]
			tries_letters.append(letter)
		else:
			print("Wrong..")
			life = life - 1
		if("-" not in hide_word):
			print("You guessed the word \"" + word + "\"\nYou survived!")
			break
		if(life == 0):
			print("You lose :(")
			break
else:
	pass