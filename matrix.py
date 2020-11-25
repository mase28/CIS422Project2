from assignment import *
from schedule import *
import math


class Event:
    def __init__(self, time, name):
        self.time = time
        self.name = name

    def __repr__(self):
        return str(self.name)


def createMatrix():
    matrix = [[0]*24 for i in range(7)]
    for a in range(7):
        for j in range(8):
            matrix[a][j] = 1
    for a in range(7):
        for j in [20,21,22,23]:
            matrix[a][j] = 1
    return matrix


"""def fill_early_group(matrix, event_list):
    events = len(event_list)
    tracker = 0
    hours_worked = 0
    for row in matrix:
        for i in range(24):
            if row[i] == 0:
                hours_worked += 1
                if hours_worked == 3:
                    hours_worked = 0
                    i += 1
                row[i] = (5, event_list[tracker].name)
                event_list[tracker].time -= 1
                if event_list[tracker].time == 0:
                    tracker += 1
                if tracker == events:
                    return matrix
"""


def fill_early_group_sched(matrix, event_list):
    events = len(event_list)
    tracker = 0
    hhours_worked = 0
    for row in matrix:
        for key in matrix[row]:
            if matrix[row][key] == "Available":
                hhours_worked += 0.5
                if hhours_worked == 2.5:
                    hhours_worked = 0
                    continue
                else:
                    matrix[row][key] = event_list[tracker]
                    event_list[tracker].time -= 0.5
                    if event_list[tracker].time == 0:
                        tracker += 1
                    if tracker == events:
                        return matrix
            else:
                hhours_worked = 0


def fill_early_split_sched(matrix, event_list):
    n = len(event_list)
    valid_events = [i for i in range(len(event_list))]
    tracker = 0
    hhoursWorked = 0
    totalHours = sum([a.time for a in event_list])
    for row in matrix:
        for key in matrix[row]:
            if hhoursWorked == 2:
                hhoursWorked = 0
            elif matrix[row][key] != "Available":
                hhoursWorked = 0
            elif matrix[row][key] == "Available" and totalHours != 0:
                while valid_events[math.floor(tracker)%n] == -1:
                    tracker += 1
                if valid_events[math.floor(tracker)%n] != -1:
                    matrix[row][key] = event_list[math.floor(tracker)%n].name
                    hhoursWorked += 0.5
                    event_list[math.floor(tracker)%n].time -= 0.5
                    totalHours -= 0.5
                    if event_list[math.floor(tracker)%n].time == 0:
                        valid_events[math.floor(tracker)%n] = -1
                    tracker += 0.5
            elif totalHours == 0:
                return matrix
            else:
                continue
    return matrix

"""
def fill_early_split(matrix, event_list):
    n = len(event_list)
    valid_events = [i for i in range(len(event_list))]
    tracker = 0
    hoursWorked = 0
    totalHours = sum([a.time for a in event_list])
    print(totalHours)
    print(valid_events)
    print(n)
    print(event_list)

    for row in matrix:
        for i in range(24):
            if hoursWorked == 2:
                hoursWorked = 0
            elif row[i] == 0 and totalHours != 0:
                while valid_events[tracker%n] == -1:
                    tracker += 1
                if valid_events[tracker%n] != -1:
                    row[i] = (5,event_list[tracker%n].name)
                    hoursWorked += 1
                    event_list[tracker%n].time -= 1
                    totalHours -= 1
                    if event_list[tracker%n].time == 0:
                        valid_events[tracker%n] = -1
                    tracker += 1
            elif totalHours == 0:
                return matrix
            else:
                continue
    return matrix
"""

Assign1 = Assignment("hw1", 10, 3.5, datetime.date.today() + datetime.timedelta(days=1), 7)
Assign2 = Assignment("hw2", 3, 0.5, datetime.date.today() + datetime.timedelta(days=3), 4)
Assign3 = Assignment("hw3", 25, 6, datetime.date.today() + datetime.timedelta(days=5), 10)
Assign4 = Assignment("hw4", 5, 1.5, datetime.date.today() + datetime.timedelta(days=2), 8)
Assign5 = Assignment("hw5", 7, 2, datetime.date.today() + datetime.timedelta(days=7), 5)

sched = Schedule()

eli = [Assign1, Assign2, Assign3, Assign4, Assign5]
print(fill_early_split_sched(sched.schedule, eli))