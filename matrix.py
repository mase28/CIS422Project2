import math
import datetime


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
    totalHours = sum([a.time for a in event_list])
    for row in matrix:
        for key in matrix[row]:
            if hhours_worked == 2.5:
                hhours_worked = 0
            elif tracker >= events-1:
                return matrix
            elif matrix[row][key] != "Available":
                hhours_worked = 0
            elif matrix[row][key] == "Available" and totalHours != 0:
                hhours_worked += 0.5
                matrix[row][key] = event_list[tracker].name
                print(f"day: {matrix[row]}, time: {matrix[row][key]}, value: {matrix[row][key]}")
                event_list[tracker].time -= 0.5
                if event_list[tracker].time == 0:
                    tracker += 1
            elif totalHours == 0:
                return matrix
            else:
                continue


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

