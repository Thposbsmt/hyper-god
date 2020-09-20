board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def draw(b):
	print("""
	-------------
	| {} | {} | {} |
	| {} | {} | {} |
	| {} | {} | {} |
	-------------
	""".format(b[0][0], b[0][1], b[0][2],
			   b[1][0], b[1][1], b[1][2],
			   b[2][0], b[2][1], b[2][2]))

def player_input(token):
	valid = False
	while not valid:
		x = input("Player " + token + " play.\nInput coord x: ")
		y = input("Input coord y: ")
		try:
			x = int(x)
			y = int(y)
		except:
			print("ERROR Try again")
			continue
		if(x in range(1, 4) and y in range(1, 4)):
			if(str(board[y-1][x-1]) not in "XO"):
				board[y-1][x-1] = token
				valid = True
			else:
				print("This cell is already taken. Try again")
		else:
			print("Uncorrect input. Try again (1-3)")

def check_win(b):
    if(b[0][0] == b[0][1] == b[0][2]):
    	return b[0][0] 
    elif(b[1][0] == b[1][1] == b[1][2]):
    	return b[1][0]  
    elif(b[2][0] == b[2][1] == b[2][2]):
    	return b[2][0] 
    elif(b[0][0] == b[1][1] == b[2][2]):
    	return b[0][0]  
    elif(b[2][0] == b[1][1] == b[0][2]):
    	return b[2][0] 
    elif(b[0][0] == b[1][0] == b[2][0]):
    	return b[0][0] 
    elif(b[0][1] == b[1][1] == b[2][1]):
    	return b[0][1] 
    elif(b[0][2] == b[1][2] == b[2][2]):
    	return b[0][2] 
    else:
    	return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw(board)
        if counter % 2 == 0:
            player_input("X")
        else:
            player_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp + " player win!")
                win = True
                break
        if counter == 9:
            print("Draw!")
            break
    draw(board)

main(board)