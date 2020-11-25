import datetime
import copy
from assignment import *

"""     
        self.name = name
		self.percent = percent
		self.time = length
		self.due = dueDate
		self.priority = priority
		self.notes = info
		"""


def convertdate(d):
    a = datetime.date.today()
    times = d[1].split(":")
    hour = int(times[0])
    minute = int(times[1])
    new_val = datetime.datetime(a.year, a.month, a.day, hour, minute, 0, 0)
    days = 0 - new_val.weekday()
    if days <=0:
        days += 7
    fin_val = new_val + datetime.timedelta(days)
    if d[0] == "Monday":
        return fin_val
    elif d[0] == "Tuesday":
        return fin_val + datetime.timedelta(1)
    elif d[0] == "Wednesday":
        return fin_val + datetime.timedelta(2)
    elif d[0] == "Thursday":
        return fin_val + datetime.timedelta(3)
    elif d[0] == "Friday":
        return fin_val + datetime.timedelta(4)
    elif d[0] == "Saturday":
        return fin_val + datetime.timedelta(5)
    else:
        return fin_val + datetime.timedelta(6)



def sortbyDueDate(AssignmentList):
    for v in AssignmentList:
        v.due = convertdate(v.due)
    for a in AssignmentList:
        dur = a.due-datetime.datetime.today()
        dur_val = (dur.total_seconds()/3600)
        a.due = dur_val
    #newAssignmentList = sorted(AssignmentList, key=lambda assign: assign.due)
    newAssignmentList = AssignmentList.copy()
    new_li = []
    for b in newAssignmentList:
        new_li.append(b.due)
    for c in newAssignmentList:
        c.due = ((-(c.due - min(new_li))/(max(new_li)-min(new_li)))+1)*10
    return newAssignmentList


def sortbyPercent(AssignmentList):
    new_li = []

    for a in AssignmentList:
        a.percent = (a.percent/(a.time*60))
    for b in AssignmentList:
        new_li.append(b.percent)
    for c in AssignmentList:
        c.percent = ((c.percent-min(new_li))/(max(new_li)-min(new_li)))*10
    #newAssignmentList = sorted(AssignmentList, key=lambda assign: assign.percent, reverse=True)
    newAssignmentList = AssignmentList
    return newAssignmentList

def sortbyLong(AssignmentList):
    new_li = []
    for a in AssignmentList:
        new_li.append(a.time)
    for b in AssignmentList:
        b.timeval = ((b.time-min(new_li))/(max(new_li)-min(new_li)))*10
    #newAssignmentList = sorted(AssignmentList, key=lambda assign: assign.time, reverse=True)
    newAssignmentList = AssignmentList
    return newAssignmentList

def sortbyShort(AssignmentList):
    new_li = []
    for a in AssignmentList:
        new_li.append(a.time)
    for b in AssignmentList:
        b.timeval = ((-(b.time - min(new_li))/(max(new_li)-min(new_li)))+1)*10
    #newAssignmentList = sorted(AssignmentList, key=lambda assign: assign.time, reverse=True)
    newAssignmentList = AssignmentList
    return newAssignmentList


def sortMechanism(AssignmentList):
    val = copy.deepcopy(AssignmentList)
    v1 = copy.deepcopy(AssignmentList)
    v2 = copy.deepcopy(AssignmentList)
    val1 = sortbyDueDate(v1)
    val2 = sortbyPercent(v2)
    for i in range(len(val)):
        val[i].percent = val2[i].percent
        val[i].due = val1[i].due
    return val

def prior_stand(AssignmentList):
    new = sortMechanism(AssignmentList)
    new_val = sorted(new.copy(), key=lambda assign: assign.percent*0.2+assign.due*0.5+assign.priority*0.3, reverse=True)
    return new_val

def prior_earl(AssignmentList):
    A1 = copy.deepcopy(AssignmentList)
    A2 = copy.deepcopy(AssignmentList)
    new = sortMechanism(A1)
    ti = sortbyShort(A2)
    for i in range(len(new)):
        new[i].timeval = ti[i].timeval
    new_val = sorted(new, key=lambda assign: assign.due*0.5+assign.timeval*0.3+assign.priority*0.1+assign.percent*0.1, reverse=True)
    return new_val


def prior_late(AssignmentList):
    A1 = copy.deepcopy(AssignmentList)
    A2 = copy.deepcopy(AssignmentList)
    new = sortMechanism(A1)
    ti = sortbyLong(A2)
    for i in range(len(new)):
        new[i].timeval = ti[i].timeval
    new_val = sorted(new, key=lambda  assign: assign.due*0.5+assign.timeval*0.3+assign.priority*0.1+assign.percent*0.1, reverse=True)
    return new_val



Assign1 = Assignment("hw1", 10, 3.5, ("Monday", "11:30"), 7)
Assign2 = Assignment("hw2", 3, 0.5, ("Wednesday", "18:00"), 4)
Assign3 = Assignment("hw3", 25, 6, ("Friday", "17:00"), 10)
Assign4 = Assignment("hw4", 5, 1.5, ("Tuesday", "15:30"), 8)
Assign5 = Assignment("hw5", 7, 2, ("Sunday", "18:00"), 5)

li = [Assign1, Assign2, Assign3, Assign4, Assign5]
val1 = copy.deepcopy(li)
val2 = copy.deepcopy(li)
val3 = copy.deepcopy(li)




