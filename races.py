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

class Race():
	def __init__(self, str, agi, int, con):
		self.starting_stats = Stats(str, agi, int, con)
		if not self.starting_stats.validStart():
			raise InvalidStartingStats("Unbalanced starting stats: %d" % self.starting_stats.sum())


	def validStartingStats(self):
		return sum(self.starting_stats.values()) == 40


class Human(Race):
	def __init__(self):
		super().__init__(str=10, agi=10, int=10, con=10)


class Dwarf(Race):
	def __init__(self):
		super().__init__(str=12, agi=8, int=8, con=12)


class Elf(Race):
	def __init__(self):
		super().__init__(str=8, agi=12, int=12, con=8)


class Halfling(Race):
	def __init__(self):
		super().__init__(str=8, agi=12, int=10, con=10)


class Goblin(Race):
	def __init__(self):
		super().__init__(str=8, agi=14, int=8, con=10)


class Ogre(Race):
	def __init__(self):
		super().__init__(str=14, agi=6, int=6, con=14)


class Drow(Elf):
	pass