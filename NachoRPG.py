#!/usr/bin/env python3
import random

races = {
	"human" : {
		"starting stats" : {
			"str" : 10,
			"agi" : 10,
			"int" : 10,
			"con" : 10,
		}
	},
	"elf" : "",
	"halfling" : "",
	"goblin" : "",
	"ogre" : "",
}

	# Character Creation
class Character(object):
	def __init__(self, name, race, className):
		self.name = name
		self.race = race
		self.className = className
		self.stats = races[race]["starting stats"]
		self.hp = self.stats["con"] * 1.5
		self.mp = self.stats["int"] * 1.5


	def sayHello(self):
		print("Hello, my name is %s! Nice to meet you." % (self.name))
		print("Class : %s" % (self.className))
		print("Race : %s" % (self.race))
		print("Stats : %s" % (self.stats))
		print("Current HP : %s" % (self.hp))
		print("Current MP : %s" % (self.mp))

	def attack(self, target):
		# str vs target con = target reduced hp
		my_str = self.stats["str"]
		tar_con = target.stats["con"]
		damage = (my_str + random.randint(1,6)) - tar_con
		print("%s attacks %s. %s takes %d damage" % (self.name, target.name, target.name, damage))
		target.takeDamage(damage)

	def takeDamage(self, value):
		self.hp = self.hp - value
		print ("%s is at %d HP!"  % (self.name, self.hp))



	# Moves
	# Inventory

hero = Character("Deku", "human", "hero")
hero.sayHello()

villan = Character("Nomu", "human", "villan")
villan.sayHello()

hero.attack(villan)
