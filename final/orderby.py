# Big O of n^2
def order_fname(alist, asc=False):
    newlist = alist
    if asc:
        for x in range(len(newlist) - 1, -1, -1):
            noswaps = True
            # up to but not including x
            for i in range(x):
                if newlist[i].fname > newlist[i + 1].fname:
                    newlist[i], newlist[i + 1] = newlist[i + 1], newlist[i]
                    noswaps = False
            if noswaps:
                break
    else:
        for x in range(len(newlist) - 1, -1, -1):
            noswaps = True
            # up to but not including x
            for i in range(x):
                if newlist[i].fname < newlist[i + 1].fname:
                    newlist[i], newlist[i + 1] = newlist[i + 1], newlist[i]
                    noswaps = False
            if noswaps:
                break
    return newlist


def order_lname(alist, asc=False):
    newlist = alist
    if asc:
        for x in range(len(newlist) - 1, -1, -1):
            noswaps = True
            # up to but not including x
            for i in range(x):
                if newlist[i].lname > newlist[i + 1].lname:
                    newlist[i], newlist[i + 1] = newlist[i + 1], newlist[i]
                    noswaps = False
            if noswaps:
                break
    else:
        for x in range(len(newlist) - 1, -1, -1):
            noswaps = True
            # up to but not including x
            for i in range(x):
                if newlist[i].lname < newlist[i + 1].lname:
                    newlist[i], newlist[i + 1] = newlist[i + 1], newlist[i]
                    noswaps = False
            if noswaps:
                break
    return newlist

def order_age(alist, asc=False):
    newlist = alist
    if asc:
        for x in range(len(newlist) - 1, -1, -1):
            noswaps = True
            # up to but not including x
            for i in range(x):
                if newlist[i].age > newlist[i + 1].age:
                    newlist[i], newlist[i + 1] = newlist[i + 1], newlist[i]
                    noswaps = False
            if noswaps:
                break
    else:
        for x in range(len(newlist) - 1, -1, -1):
            noswaps = True
            # up to but not including x
            for i in range(x):
                if newlist[i].age < newlist[i + 1].age:
                    newlist[i], newlist[i + 1] = newlist[i + 1], newlist[i]
                    noswaps = False
            if noswaps:
                break
    return newlist

def order_salary(alist, asc=False):
    newlist = alist
    if asc:
        for x in range(len(newlist) - 1, -1, -1):
            noswaps = True
            # up to but not including x
            for i in range(x):
                if newlist[i].salary > newlist[i + 1].salary:
                    newlist[i], newlist[i + 1] = newlist[i + 1], newlist[i]
                    noswaps = False
            if noswaps:
                break
    else:
        for x in range(len(newlist) - 1, -1, -1):
            noswaps = True
            # up to but not including x
            for i in range(x):
                if newlist[i].salary < newlist[i + 1].salary:
                    newlist[i], newlist[i + 1] = newlist[i + 1], newlist[i]
                    noswaps = False
            if noswaps:
                break
    return newlist


order_by = [
    order_fname,
    order_lname,
    order_age,
    order_salary
]
