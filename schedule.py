from assignment import *

class Schedule(object):
	"""docstring for Schedule"""
	def __init__(self):
		self.schedule = {}
		self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		for i in range(7):
			self.schedule[self.days[i]] = {}
			for j in range(24):
				time1 = str(j)
				time2 = str(j) + ":30"
				self.schedule[self.days[i]][time1] = "available"
				self.schedule[self.days[i]][time2] = "available"

	def add_assignment(self, assignment, day, time1, time2):
		flag = False
		for time in self.schedule[day]:
			if time == time1:
				flag = True
			elif time == time2:
				flag = False
			
			if flag:
				self.schedule[day][time] = assignment

	def generate_schedule(self):
		return

	def add_sleep(self, day, time1, time2):
		flag = False
		if day == "Sunday":
			next_day = "Monday"
		else:
			for d in range(len(self.days)):
				if self.days[d] == day:
					next_day = self.days[d+1]
		for time in self.schedule[day]:
			if time == time1:
				flag = True
			elif time == time2:
				flag = False

			if flag:
				self.schedule[day][time] = "Unavailable"
		for time in self.schedule[next_day]:
			if time == time2:
				flag = False

			if flag:
				self.schedule[next_day][time] = "Unavailable"

	def add_break(self, day, time1, time2):
		flag = False
		for time in self.schedule[day]:
			if time == time1:
				flag = True
			elif time == time2:
				flag = False
			
			if flag:
				self.schedule[day][time] = "Unavailable"

	def __str__(self):
		return str(self.schedule)

	def __repr__(self):
		return "Schedule"

		

if __name__ == "__main__":
	A = Schedule()
	A.add_break("Sunday", "12:30", "15")
	hw1 = Assignment("Homework1", 7.5, 3, "Algebra Homework")
	print(hw1)
	A.add_assignment(hw1, "Monday", "2", "6:30")
	print(A)