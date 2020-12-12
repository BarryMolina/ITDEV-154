def sort_fname(alist, asc=False):
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


def sort_lname(alist, asc=False):
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

def sort_age(alist, asc=False):
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

def sort_salary(alist, asc=False):
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


sort_by = [
    sort_fname,
    sort_lname,
    sort_age,
    sort_salary
]
