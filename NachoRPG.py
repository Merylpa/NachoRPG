#!/usr/bin/env python3
import random
import save_game
from character import Character, PlayerCharacter, Enemy
import races
import fmt
#GOALS - Accuracy
#GOALS - Attack types
#GOALS - Crit chance

title_screen = """
,---.   .--.   ____        _______   .---.  .---.     ,-----.    .-------.    .-------.   .-_'''-.    
|    \  |  | .'  __ `.    /   __  \  |   |  |_ _|   .'  .-,  '.  |  _ _   \   \  _(`)_ \ '_( )_   \   
|  ,  \ |  |/   '  \  \  | ,_/  \__) |   |  ( ' )  / ,-.|  \ _ \ | ( ' )  |   | (_ o._)||(_ o _)|  '  
|  |\_ \|  ||___|  /  |,-./  )       |   '-(_{;}_);  \  '_ /  | :|(_ o _) /   |  (_,_) /. (_,_)/___|  
|  _( )_\  |   _.-`   |\  '_ '`)     |      (_,_) |  _`,/ \ _/  || (_,_).' __ |   '-.-' |  |  .-----. 
| (_ o _)  |.'   _    | > (_)  )  __ | _ _--.   | : (  '\_/ \   ;|  |\ \  |  ||   |     '  \  '-   .' 
|  (_,_)\  ||  _( )_  |(  .  .-'_/  )|( ' ) |   |  \ `"/  \  ) / |  | \ `'   /|   |      \  `-'`   |  
|  |    |  |\ (_ o _) / `-'`-'     / (_{;}_)|   |   '. \_/``".'  |  |  \    / /   )       \        /  
'--'    '--' '.(_,_).'    `._____.'  '(_,_) '---'     '-----'    ''-'   `'-'  `---'        `'-...-'   
                                                                                                      
"""
print(title_screen)

saves = save_game.find_saves()
new_game = False
if saves:
	print("0) New Game")
	for index, filename in enumerate(saves, 1):
		print("{}) {}".format(index, filename))
	choice = int(input("Choose : ")) - 1 
	if choice == -1:
		new_game = True
	else:
		hero = save_game.load_save(saves[choice])
else:
	new_game = True

if new_game:
	player_name = input("Enter your name: ")
	character_name = input("Enter your hero's name: ")
	hero = PlayerCharacter(character_name, races.Human, "hero", player_name, catch_phrase = "Go beyond! Plus Ultra!")
	hero.sayHello()

print("Welcome to the game %s" % (hero.player_name))

villan = Enemy("Nomu", races.Human, "villan", catch_phrase = "...")

while True:
	
	villan.sayHello()

	while True:
		if hero.hp > 0:
			hero.choose_action(villan)
		if villan.hp > 0:
			villan.choose_action(hero)

		if hero.hp <= 0 or villan.hp <= 0:
			break

	if hero.hp > 0:
		print("Hero wins!")
		hero.combatExperience(villan)
	if villan.hp > 0:
		print("Evil wins!")
		villan.combatExperience(hero)
	# Reset character HP
	hero.hpReset()
	villan.hpReset()

	choice = input("Would you like to see your character sheet? y/n \n")
	if "y" in choice.lower():
		hero.printCharacterSheet()

	choice = input("Would you like to save your game? y/n \n")
	if "y" in choice.lower():
		filename = "{}_{}.save".format(hero.player_name, hero.name)
		save_game.create_save(hero, filename)

	choice = input(fmt.blue("Would you like to continue (y/n) \n"))
	if "n" in choice.lower():
		break
