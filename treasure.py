print(f'''
	*******************************************************************************
			|                   |                  |                     |
	_________|________________.=""_;=.______________|_____________________|_______
	|                   |  ,-"_,=""     `"=.|                  |
	|___________________|__"=._o`"-._        `"=.______________|___________________
			|                `"=._o`"=._      _`"=._                     |
	_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
	|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
	|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
			|           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
	_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
	|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
	|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
	____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
	/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
	____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
	/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
	____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
	/______/______/______/______/______/______/______/______/______/______/_____ /
	*******************************************************************************
''')
print(f"Welcome to Treasure Island.")
print(f"Your mission is to find the treasure.")

first = input(f"Left or Right?\n").lower()
if first == "left":
	second = input(f"Swin or Wait?\n").lower()
	if second == "wait":
		third = input(f"Which door? (Red / Blue / Yellow)\n").lower()
		if(third == "yellow"):
			print(f"\nCongratulations...You Win!")
		else:
			print(f"\nGame Over.")
	else:
		print(f"\nGame Over.")
else:
	print(f"\nGame Over.")