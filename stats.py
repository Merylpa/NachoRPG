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