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


def sortbyDueDate(AssignmentList):
    for a in AssignmentList:
        dur = a.due-datetime.date.today()
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
        b.time = ((b.time-min(new_li))/(max(new_li)-min(new_li)))*10
    #newAssignmentList = sorted(AssignmentList, key=lambda assign: assign.time, reverse=True)
    newAssignmentList = AssignmentList
    return newAssignmentList

def sortbyShort(AssignmentList):
    new_li = []
    for a in AssignmentList:
        new_li.append(a.time)
    for b in AssignmentList:
        b.time = b.time = ((-(b.time - min(new_li))/(max(new_li)-min(new_li)))+1)*10
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
        new[i].time = ti[i].time
    new_val = sorted(new, key=lambda assign: assign.due*0.5+assign.time*0.3+assign.priority*0.1+assign.percent*0.1, reverse=True)
    return new_val


def prior_late(AssignmentList):
    A1 = copy.deepcopy(AssignmentList)
    A2 = copy.deepcopy(AssignmentList)
    new = sortMechanism(A1)
    ti = sortbyLong(A2)
    for i in range(len(new)):
        new[i].time = ti[i].time
    new_val = sorted(new, key=lambda  assign: assign.due*0.5+assign.time*0.3+assign.priority*0.1+assign.percent*0.1, reverse=True)
    return new_val


def priority_early(AssignmentList):
    l1 = sorted([((a.percent / (a.time * 60)), a.name, a.priority, a.time) for a in AssignmentList], reverse=True)
    l2 = [((val[0] * (10 / l1[0][0])), val[1], val[2], val[3]) for val in l1]
    l3 = [(val[0] * 0.40 + val[2] * 0.60 + (1 / val[3]) * 10, val[1]) for val in l2]
    print(sorted(l3, reverse=True))

def priority_long(AssignmentList):
    l1 = sorted([((a.percent / (a.time * 60)), a.name, a.priority, a.time) for a in AssignmentList], reverse=True)
    l2 = [((val[0] * (10 / l1[0][0])), val[1], val[2], val[3]) for val in l1]
    l3 = [(val[0] * 0.40 + val[2] * 0.60 + val[3], val[1]) for val in l2]
    print(sorted(l3, reverse=True))

    return 0


Assign1 = Assignment("hw1", 10, 3.5, datetime.date.today() + datetime.timedelta(days=1), 7, None)
Assign2 = Assignment("hw2", 3, 0.5, datetime.date.today() + datetime.timedelta(days=3), 4, None)
Assign3 = Assignment("hw3", 25, 6, datetime.date.today() + datetime.timedelta(days=5), 10, None)
Assign4 = Assignment("hw4", 5, 1.5, datetime.date.today() + datetime.timedelta(days=2), 8, None)
Assign5 = Assignment("hw5", 7, 2, datetime.date.today() + datetime.timedelta(days=7), 5, None)

li = [Assign1, Assign2, Assign3, Assign4, Assign5]
val1 = copy.deepcopy(li)
val2 = copy.deepcopy(li)
val3 = copy.deepcopy(li)
#priority_standard(li)
#priority_early(li)
#priority_long(li)



aas = prior_stand(val1)

for a in aas:
    print(a.name + ": " +  str(a.time))

print("\n")

aat = prior_earl(val2)
for b in aat:
    print(b.name + ": " + str(b.time))

print("\n")

aau = prior_late(val3)
for c in aau:
    print(c.name + ": " + str(c.time))



