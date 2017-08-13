import utilities
from stats import Stats


class Race(metaclass=utilities.StrMeta):
	starting_stats = Stats(0,0,0,0)

	def __init__(self, str, agi, int, con):
		if not self.starting_stats.validStart():
			raise InvalidStartingStats("Unbalanced starting stats: %d" % self.starting_stats.sum())

class Human(Race):
	starting_stats = Stats(str=10, agi=10, int=10, con=10)


class Dwarf(Race):
	starting_stats = Stats(str=12, agi=8, int=8, con=12)


class Elf(Race):
	starting_stats = Stats(str=8, agi=12, int=12, con=8)


class Halfling(Race):
	starting_stats = Stats(str=8, agi=12, int=10, con=10)


class Goblin(Race):
	starting_stats = Stats(str=8, agi=14, int=8, con=10)


class Ogre(Race):
	starting_stats = Stats(str=14, agi=6, int=6, con=14)


class Drow(Elf):
	pass