class Assignment(object):

	def __init__(self, name, percent, length, info):
		self.name = name
		self.worth = percent
		self.time = length
		self.notes = info

	def __str__(self):
		return self.name

	def __repr__(self):
		return "Assignment"