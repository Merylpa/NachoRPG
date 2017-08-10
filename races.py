class InvalidStartingStats(Exception):
	pass

class Stats():
	def __init__(self, str, agi, int, con):
		self.str = str
		self.agi = agi
		self.int = int
		self.con = con

	def sum(self):
		return sum([self.str, self.agi, self.int, self.con])

	def validStart(self):
		return self.sum() == 40

	def __str__(self):
		return """Strength      : {s.str}
Agility       : {s.agi}
Intelligence  : {s.int}
Constitution  : {s.con}
""".format(s=self)	

	def __repr__(self):
		return str(vars(self))

class RaceMeta(type):
	"""
	Enables useful str representation of races without having to create instances
	of objects or needless attributes
	"""
	def __str__(self):
		return self.__name__

class Race(metaclass=RaceMeta):
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