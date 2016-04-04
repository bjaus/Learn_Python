from random import choice

cave_numbers = range(1,21)
wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or
	player_location == wumpus_friend_location):
	player_location = choice(cave_numbers) 
	
print("Welcome to Hunt the Wumpus!")
print("You can see {} caves".format(len(cave_numbers)))
print("To play, just type the number")
print("of the cave you wish to enter next")

while True:
	print("You are in cave {}".format(player_location))
	if (player_location == wumpus_location - 1 or
		player_location == wumpus_location + 1):
		print("I smell a wumpus!")
	if (player_location == wumpus_friend_location - 1 or
		player_location == wumpus_friend_location + 1):
		print("I smell a wumpus!")
		
	print("Which cave next?")
	player_input = input(">")
	if (not player_input.isdigit() or
		int(player_input) not in cave_numbers):
		print("{} is not a cave!".format(player_input))
	else:
		player_location = int(player_input)
		if player_location == wumpus_location:
			print("Aargh! You got eaten by a wumpus!")
			break
		if player_location == wumpus_friend_location:
			print("Aargh! You got eaten by the wumpus' friend!")
			break