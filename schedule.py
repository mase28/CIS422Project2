from assignment import *
from priority import *
import sys

class Schedule(object):
	"""docstring for Schedule"""
	def __init__(self):
		self.schedule = {}
		self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		self.assignments = []
		self.unassigned = []
		self.matrix = ""
		self.priority = ""
		for i in range(7):
			self.schedule[self.days[i]] = {}
			for j in range(0, 24):
				time1 = str(j).zfill(2)
				time2 = str(j).zfill(2) + ":30"
				self.schedule[self.days[i]][time1] = "Available"
				self.schedule[self.days[i]][time2] = "Available"

	def add_assignment(self, assignment):
		self.assignments.append(assignment)

	def __prioritize_assignments(self):
		self.assignments = sorted(self.assignments, key=lambda assignment: (assignment.percent/assignment.time), reverse=True)

	def __generate_schedule(self):
		self.__prioritize_assignments()
		i = 0
		flag = False
		while i < len(self.assignments):
			assignment = self.assignments[i]
			day = assignment.due[0]
			for time in reversed(self.schedule[day]):
				if time == assignment.due[1]:
					flag = True
					continue

				if flag:
					if self.schedule[day][time] == "Available":
						self.schedule[day][time] = assignment.name
						assignment.time -= .5

					if assignment.time == 0:
						flag = False
						i += 1
						break
			
			if assignment.time != 0:
				if day == "Monday":
					self.unassigned.append(assignment)
					flag = False
					i += 1
				else: 
					for d in range(len(self.days)):
						if self.days[d] == day:
							prev_day = self.days[d-1]
					assignment.due = (prev_day, assignment.due[1])

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
				self.schedule[day][time] = "Sleep"
		for time in self.schedule[next_day]:
			if time == time2:
				flag = False

			if flag:
				self.schedule[next_day][time] = "Sleep"

	def add_break(self, day, name, time1, time2):
		flag = False
		for time in self.schedule[day]:
			if time == time1:
				flag = True
			elif time == time2:
				flag = False
			
			if flag:
				self.schedule[day][time] = name

	def __str__(self):
		return str(self.schedule)

	def __repr__(self):
		return "Schedule"

	def __insert_blanks(self):
		for day in self.schedule:
			for time in self.schedule[day]:
				if self.schedule[day][time] == "Available":
					self.schedule[day][time] = ""

	def create_calendar(self):
		self.__generate_schedule()
		self.__insert_blanks()
		output_first = (
    	"""
    	<!DOCTYPE html>
		<html>
		<head>
		<style>
		table {
  			font-family: arial, sans-serif;
  			border-collapse: collapse;
  		width: 100%;
		}

		td, th {
		  border: 1px solid #dddddd;
		  text-align: left;
		  padding: 8px;
		}

		tr:nth-child(even) {
		  background-color: #dddddd;
		}
		</style>
		</head>
		<body>

		<h2>Calendar</h2>

		<table>
		  <tr>
		  	<th>Time</th>
		    <th>Monday</th>
		    <th>Tuesday</th>
		    <th>Wednesday</th>
		    <th>Thursday</th>
		    <th>Friday</th>
		    <th>Saturday</th>
		    <th>Sunday</th>
		  </tr>
		""")

		output_last = (
    	"""
    	</table>

    	<p>Press return to return to the home page and restart</p>
    	<a href="/" class="btn btn-primary" type="button">Return</a>

		</body>
		</html>
		""")

		earliest = ""
		bedtime = ""
		current = 0
		least = 49
		latest = 0
		for day in self.schedule:
			for time in self.schedule[day]:
				if self.schedule[day][time] == "Sleep":
					current += 1
					if current > least:
						if current > latest:
							bedtime = time
							latest = current
							current = 0
							break
						else:
							current = 0
							break
				elif current < least:
					earliest = time 
					least = current
					current += 1
				else:
					current += 1

		flag = False
		for time in self.schedule["Monday"]:
			if time == earliest:
				flag = True
			elif time == bedtime:
				flag = False
			if flag:
				row = (
					f"""
					  <tr>
					    <td>{time}</td>
					    <td>{self.schedule["Monday"][time]}</td>
					    <td>{self.schedule["Tuesday"][time]}</td>
					    <td>{self.schedule["Wednesday"][time]}</td>
					    <td>{self.schedule["Thursday"][time]}</td>
					    <td>{self.schedule["Friday"][time]}</td>
					    <td>{self.schedule["Saturday"][time]}</td>
					    <td>{self.schedule["Sunday"][time]}</td>
					  </tr>
					""")
				output_first += row
		
		output_sec = ""
		if len(self.unassigned) > 0:
			missed_assignments = ""
			for assignment in self.unassigned:
				missed_assignments += (str(assignment) + ", ")
			output_sec = f"<p>The assignments, {missed_assignments}were not scheduled for their full duration because either other higher priority assignments were scheduled first, or due to the breaks and sleep schedule, there wasn't enough time available to schedule them.</p>"

		output_first += (output_sec + output_last)

		f = open("templates/output.html", "w")
		f.write(output_first)
		f.close()
