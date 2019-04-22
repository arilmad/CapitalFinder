# Made by Arild Madshaven 19. April 2019
# Feel free to use for private purposes after 22. April 2019 ;)
# Credit owner.

import numpy as np

CAPS = []

FoundCaps = []

BOARD = [
['g','v','r','s','t','j','g','a','s','n'],
['h','m','a','u','e','o','m','d','i','p'],
['i','n','n','m','o','o','a','l','p','u'],
['a','i','o','s','r','k','r','r','r','l'],
['s','l','l','i','a','e','a','i','i','d'],
['a','o','a','r','b','h','g','m','i','a'],
['j','k','l','a','a','a','a','l','i','b'],
['u','h','k','p','t','l','i','f','a','e'],
['b','u','k','i','e','v','o','p','m','r'],
['a','v','u','s','n','s','p','u','a','n']
]

def reader():

#	special purpose reader fit for the capitals.txt format
	f = open('capitals.txt', 'r')
	global CAPS

	lines = f.readlines()
	for line in lines:

#		ignore garbage lines
		if line == '\n' or line == 'Ingen\n':
			continue

#		ad hoc sol for skipping lines such as 'På M:''
		if line[0] == 'P' and line[1] == 'å':
			continue

#		skip lines such as '4 bokstaver'
		try:
			a = (int)(line[0])
			continue

		except:
			word = ''

			for letter in line:

#				every cap is listed like 'Oslo (Europa)'. We don't want the latter part
				if letter == '(':
					break

#				convert e.g. 'La Paze' to 'lapaze' to fit borad format
				if letter != ' ':
					word += letter.lower()

			CAPS.append(word)

#			nice spot to check whether the capitals are extracted perfectly :)
#			print(word)

	f.close()

def findCaps(_list):

	no = 0

#	a list such as 'abcd' will be checked at a ab abc abcd b bc bcd c cd d 
#	and then flipped to dcba and checked likewise
	for direction in range(2):

		word = ''

		for i in range(len(_list)):

			for j in range(len(_list) - i):

				word += _list[i+j]

				if word in CAPS and word not in FoundCaps:
					print("(findCaps) FOUND word", word, "ending at pos", i+j, "in list", _list)
					FoundCaps.append(word)
					no += 1

			word = ''

		_list = np.flip(_list)

	return no
		

def main():

	no = 0
	board = np.array(BOARD)
	
	reader()

	print("(main) reader read\n")
	print("(main) number of capitals loaded:", len(CAPS))

#	check rows
	print("(main) scanning rows..\n")

	for row in board:
		no += findCaps(row)	

#	check columns
	print("\n(main) scanning cols..\n")

	for column in board.T:
		no += findCaps(column)

#	check diagonals
	print("\n(main) scanning diags..\n")

#	np.diag uses input argument to fetch diagonals skewed from center
	midToEdge = np.size(board[0])

	for i in range(midToEdge):

#		above mid
		diagonal = np.diag(board, i)
		no += findCaps(diagonal)

#		below mid
		diagonal = np.diag(board, -i)
		no += findCaps(diagonal)


#	copying the board and rotating it by 90 deg to check opposite diagonals	
	rotB = np.rot90(board)

	print("\n(main) scanning other diags..\n")

	for i in range(midToEdge):

#		above mid	
		diagonal = np.diag(rotB, i)
		no += findCaps(diagonal)

#		below mid
		diagonal = np.diag(rotB, -i)
		no += findCaps(diagonal)
		

	print("\nno:", no, '\n')
	print("Caps found:\n", np.sort(FoundCaps), '\n')
	print("(main) exit\n")

main()
