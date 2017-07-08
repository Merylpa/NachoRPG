#!/usr/bin/env python3
import random
from character import Character, PlayerCharacter, Enemy
#GOALS - Accuracy
#GOALS - Attack types
#GOALS - Save file
#GOALS - Colors for readability

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

player_name = input("Enter your name: ")
character_name = input("Enter your hero's name: ")

print("Welcome to the game %s" % (player_name))

hero = PlayerCharacter(character_name, "human", "hero", player_name)
hero.catch_phrase = "Go beyond! Plus Ultra!"
hero.sayHello()

villan = Enemy("Nomu", "human", "villan")
villan.catch_phrase = "..."
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
if villan.hp > 0:
	print("Evil wins!")


