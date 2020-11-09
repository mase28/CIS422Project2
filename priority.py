import datetime

class Assignment:

    def __init__(self, name, time, date, percent, rating):
        self.name = name
        self.time = time
        self.dueDate = date
        self.percent = percent
        self.rating = rating


def sortbydueDate(AssignmentList):
    dueDates = [(a.dueDate, a.name) for a in AssignmentList]
    return sorted(dueDates)


def priority_standard(AssignmentList):
    l1 = sorted([((a.percent/(a.time*60)),a.name,a.rating, a.time) for a in AssignmentList], reverse=True)
    print(l1)
    l2 = [((val[0]*(10/l1[0][0])), val[1], val[2], val[3]) for val in l1]
    print(l2)
    l3 = [(val[0]*0.40 + val[2]*0.60 + (1/val[3])*10, val[1]) for val in l2]
    print(sorted(l3, reverse=True))

def priority_early(AssignmentList):
    short = []
    for a in AssignmentList:
        if a.time < 2:
            short.append((a.time, a.name))
    new_short = sorted(short)
    print(new_short)
    l1 = sorted([((a.percent / (a.time * 60)), a.name, a.rating) for a in AssignmentList], reverse=True)
    print(l1)
    l2 = [((val[0] * (10 / l1[0][0])), val[1], val[2]) for val in l1]
    print(l2)
    l3 = [(val[0] * 0.40 + val[2] * 0.60, val[1]) for val in l2]
    print(sorted(l3, reverse=True))





Assign1 = Assignment("hw1", 3.5, datetime.date.today() + datetime.timedelta(days=1), 10, 7)
Assign2 = Assignment("hw2", 0.5, datetime.date.today() + datetime.timedelta(days=3), 3, 4)
Assign3 = Assignment("hw3", 6, datetime.date.today() + datetime.timedelta(days=5), 25, 10)
Assign4 = Assignment("hw4", 1.5, datetime.date.today() + datetime.timedelta(days=2), 5, 8)
Assign5 = Assignment("hw5", 2, datetime.date.today() + datetime.timedelta(days=7), 7, 5)


li = [Assign1,Assign2,Assign3,Assign4,Assign5]

#priority_standard(li)
priority_early(li)

wa = [1,2,3,4]
print(len(wa))