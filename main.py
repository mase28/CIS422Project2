from schedule import *
from assignment import *

def main(sleep: (int, int), breaks: list, assignments: list):
	sched = Schedule()
	sched.add_sleep("Monday", "23", "6:30")
	sched.add_sleep("Tuesday", "22", "9:30")
	sched.add_sleep("Wednesday", "21", "8:30")
	sched.add_sleep("Thursday", "23", "5:30")
	sched.add_sleep("Friday", "23", "6:30")
	sched.add_sleep("Saturday", "23", "6:30")
	sched.add_sleep("Sunday", "23", "6:30")

	for i in range(len(breaks)):
		for j in range(len(breaks[i])):
			sched.add_break(sched.days[i], breaks[i][j][0], breaks[i][j][1])

	for a in assignments:
		sched.add_assignment(a)

	sched.create_calendar()




if __name__ == "__main__":
	hw1 = Assignment("Homework1", 7.5, 3, ("Thursday", "24"), "Algebra Homework")
	hw2 = Assignment("Homework2", 6, 2, ("Monday", "8"), "Psycology Homework")
	hw3 = Assignment("Homework3", 10, 1, ("Sunday", "12"), "CIS quiz")
	hw4 = Assignment("Homework4", 8, 2, ("Tuesday", "8:30"), "Algebra Midterm")
	main(("22", "7:30"), [[("10", "12:30")], [("10", "12:30"), ("14", "16:30")], [], [("14", "16:30")], [], [], []], [hw1, hw2, hw3, hw4])