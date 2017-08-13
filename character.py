import random
import fmt
import races
from races import Stats

	# Character Creation
class Character(object):
	def __init__(self, name, Race, job, catch_phrase=None):
		self.name = name
		self.race = Race
		self.job = job
		self.stats = self.race.starting_stats
		self.max_hp = self.stats.con * 1.5
		self.max_mp = self.stats.int * 1.5
		self.hp = self.max_hp
		self.mp = self.max_mp

		if catch_phrase is None:
			self.catch_phrase = fmt.blue("Hello, my name is %s! Nice to meet you." % (self.name))
		else:
			self.catch_phrase = fmt.blue(catch_phrase)

		self.status = set()
		self.actions = ["Attack", "Block"]

		# Experience and level, level up occurs every 100 xp
		self.level = 1
		self.attr_points = 0
		self.xp = 0


	def sayHello(self):
		print("%s says, \"%s\"" % (self.name, self.catch_phrase))


	def printCharacterSheet(self):
		print("""#################
Character Sheet
#################
Character Name: {s.name}
Race          : {s.race}
Class         : {s.job}
Strength      : {s.stats.str}
Agility       : {s.stats.agi}
Intelligence  : {s.stats.int}
Constitution  : {s.stats.con}
#################
""".format(s=self))

	def attack(self, target):
		self.status.discard("blocking")
		# str vs target con = target reduced hp
		damage = (self.stats.str + random.randint(1,6)) - target.stats.con

		damage = damage if damage > 1 else 1
		# prevents negative damage

		msg = fmt.yellow("%s attacks %s. for %d damage!" % (self.name, target.name, damage))
		print(msg)

		target.takeDamage(damage)

	def takeDamage(self, value):
		msg = ""
		if "blocking" in self.status:
			value = value // 2 
			msg += fmt.yellow("%s is blocking, %s only takes %d damage!\n" % (self.name, self.name, value))
		self.hp = self.hp - value
		msg += fmt.red("%s is at %d HP!"  % (self.name, self.hp))
		print(msg)

	def block(self):
		self.status.add("blocking")
		msg = "%s is blocking" % (self.name)
		print(msg)

	def hpReset(self):
		self.hp = self.max_hp

	def combatExperience(self, target_char):
		self.grantExperience(
				(target_char.level / self.level * 100)
			)


	def grantExperience(self, xp_value):
		self.xp += xp_value
		if (self.xp // 100) + 1 > self.level:
			self.levelUp()

	def levelUpMenu(self):
		"""
		Displays a menu that shows character sheet 
		Allows player to choose attributes to improve
		"""
		
		# Display available point / Select stat to increase / quit
		
		while self.attr_points > 0:
			self.printCharacterSheet
			print("Attribute points available: {}".format(self.attr_points))
			print("""
Select stat to increase
1. Strength     2. Agility
3. Intelligence 4. Constitution
0. Quit (points will be saved)
""")
			try:
				user_input = int(input(">"))
			except ValueError:
				print("Input must be a number, breaking out of menu")
				break
				
			if user_input == 1:
				self.stats.str += 1
				self.attr_points -= 1
			elif user_input == 2:
				self.stats.agi += 1
				self.attr_points -= 1
			elif user_input == 3:
				self.stats.int += 1
				self.attr_points -= 1
			elif user_input == 4:
				self.stats.con += 1
				self.attr_points -= 1
			else:
				break


	def levelUp(self):
		num_levels = int((self.xp // 100 + 1) - self.level)
		for i in range (num_levels):
			print("¡¡Ding!!")
			self.level += 1 
			self.attr_points += 2
		print(fmt.green("{s.name} is now level {s.level}".format(s=self)))
		self.levelUpMenu()


class Enemy(Character):

	def choose_action(self,target):
		""" 
		Randomly decides to attack or block
		"""
		if self.hp <= (self.max_hp / 2):
			chance = 40 
		else:
			chance = 20

		rand = random.randint(1,100)

		if rand <= chance:
			self.block()
		else:
			self.attack(target)
	
	# Moves
	# Inventory

class PlayerCharacter(Character):

	def __init__(self, name, race, job, player_name, catch_phrase=None):
		super().__init__(name, race, job, catch_phrase=catch_phrase)
		self.player_name = player_name

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


