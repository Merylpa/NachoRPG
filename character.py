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
		self.catch_phrase = "Hello, my name is %s! Nice to meet you." % (self.name)
		self.status = set()

	def sayHello(self):
		print("%s says, \"%s\"" % (self.name, self.catch_phrase))


	def printCharacterSheet(self):
		print("Class : %s" % (self.className))
		print("Race : %s" % (self.race))
		print("Stats : %s" % (self.stats))
		print("Current HP : %s" % (self.hp))
		print("Current MP : %s" % (self.mp))

	def attack(self, target):
		self.status.discard("blocking")
		# str vs target con = target reduced hp
		my_str = self.stats["str"]
		tar_con = target.stats["con"]
		damage = (my_str + random.randint(1,6)) - tar_con
		print("%s attacks %s. %s takes %d damage" % (self.name, target.name, target.name, damage))
		target.takeDamage(damage)

	def takeDamage(self, value):
		if "blocking" in self.status:
			value = value // 2 
		self.hp = self.hp - value
		print ("%s is at %d HP!"  % (self.name, self.hp))

	def block(self):
		self.status.add("blocking")



	# Moves
	# Inventory

class PlayerCharacter(Character):

	def __init__(self, name, race, className, player_name):
		super().__init__(name, race, className)
		self.player_name = player_name
		self.actions = ["Attack", "Block"]

	def choose_action(self, target):
		"""
		Allow the player to choose from various actions.
		Target may be multiple objects.
		"""
		print ("**Your Move**")
		print ("--Available Actions--")

		for index, action in enumerate(self.actions):
			print("%d ) %s" % (index + 1, action))
		#TO DO: validate input
		choice = self.actions[ int(input("Choose: ")) - 1 ]

		if choice == "Attack":
			self.attack(target)
		elif choice == "Block":
			self.block()


