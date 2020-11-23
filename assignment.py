class Assignment(object):

	def __init__(self, name, percent, length, date, info):
		self.name = name
		self.percent = percent
		self.time = length
		self.due = date
		self.notes = info

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name