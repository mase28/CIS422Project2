class Assignment(object):

	def __init__(self, name, percent, length, dueDate, priority, info):
		self.name = name
		self.percent = percent
		self.time = length
		self.due = dueDate
		self.priority = priority
		self.notes = info

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name