class StrMeta(type):
	"""
	Enables useful str representation of races without having to create instances
	of objects or needless attributes
	"""
	def __str__(self):
		return self.__name__