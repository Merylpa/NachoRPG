'''
Characters should have a Job
Starting Jobs:
	Warrior
	Rogue
	Mage

Jobs should have abilities
Jobs should have prefered Stats 
'''

import utilities
import collections

Reqs = collections.namedtuple("Reqs", "job level race")

class Ability(metaclass=utilities.StrMeta):
	"""
	Perform action, more than a basic attack
	They have requirments: level, stats, race, etc
	"""
	reqs = Reqs(None, None, None)

	def checkReqs(self, character):
		character_stuff = (character.job, character.level, character.race)
		for index, req in enumerate(self.reqs):
			if req is None:
				continue
			if req is not character_stuff[index]:
				return False
		return True


class Job(metaclass=utilities.StrMeta):
	"""
	Base job class
	"""

class Warrior(Job):
	pass


class BattleCry(Ability):
	name = "Battle Cry"
	reqs = Reqs(Warrior, None, None)





