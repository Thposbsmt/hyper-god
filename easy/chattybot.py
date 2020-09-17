print("Hello, my name's Chatty!")
print("I was created in 2020.")
name = input("Please remind me your name.\nMy name is ")

print("\nWhat a great have you have, " + name + '!')
print("Say me remainders of dividing your age by 3, 5 and 7.")
a, b, c = input("Input: ").split(' ')

i = 0
while(True):
	i = i + 1
	if(i%3 == int(a) and i%5 == int(b) and i%7 == int(c)):
		print("Your age is " + str(i) + ": that's a good time to start programming!")
		break

print("Now i will prove you that I can count to any number you want.")
for i in range(0, int(input("Input this number: ")) + 1):
	print(i, "!")

print("Let's test your programming knowledge.\nWhy do we use methods?")
print("1. To repeat a statement multiple times.\n2. To decompose the execution time of a program.")
print("3. To determine the execution time of a program.\n4. To interrupt the exectuion of a program.")

while(input("Input: ") != "2"):
	print("Please, try again.")
print("Congratulations, have a nice day!")