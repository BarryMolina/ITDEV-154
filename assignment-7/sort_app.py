
def display_list(alist):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"Current list: {alist}")
    input("\n\n Press <enter> to return to the Main Menu")


def reset(alist):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    alist = [8, 9, 1, 5, 3, 10, 2, 8]
    print(f"Current list: {alist}")
    input("\n\n Press <enter> to return to the Main Menu")

def selection_sort(alist):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    for i in range(len(alist) - 1):
        low = i
        for curr in range(i + 1, len(alist)):
            if alist[curr] < alist[low]:
                low = curr
        # if the element at index i is not already in it's proper place
        if i != low:
            alist[i], alist[low] = alist[low], alist[i]

    print(f"Sorted list: {alist}")

    input("\n\n Press <enter> to return to the Main Menu")


def bubble_sort(alist):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    # only subtract 1 because nested loop won't include highest value
    for x in range(len(alist) - 1, -1, -1):
        noswaps = True
        # up to but not including x
        for i in range(x):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                noswaps = False
        if noswaps:
            break

    print(f"Sorted list: {alist}")

    input("\n\n Press <enter> to return to the Main Menu")


def bubble_sort_comments(alist):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    # only subtract 1 because nested loop won't include highest value
    for x in range(len(alist) - 1, -1, -1):
        noswaps = True
        print(x, alist)
        # up to but not including x
        for i in range(x):
            print(f"comparing {alist[i]} and {alist[i+1]}")
            if alist[i] > alist[i + 1]:
                print(f"swapping {alist[i]} and {alist[i+1]}")
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                noswaps = False
                print(alist)
        if noswaps:
            print("breaking early")
            break

    print(f"Sorted list: {alist}")

    input("\n\n Press <enter> to return to the Main Menu")


options = [
    display_list,
    selection_sort,
    bubble_sort,
    bubble_sort_comments,
    reset,
]

def main():
    mylist = [8, 9, 1, 5, 3, 10, 2, 8]
    quit = False
    while not quit:
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "Welcome to the SortingHat app.\n"
            "\nPlease select one of the following options:\n"
            "1: Display list\n"
            "2: Sort list using selection sort\n"
            "3: Sort list using bubble sort\n"
            "4: Bubble sort with comments\n"
            "5: Reset list\n"
            "\n0: Quit\n"
        )
        choice = int(input("\n>>> "))
        print()

        if choice == 0:
            quit = True
        else:
            options[choice-1](mylist)


if __name__ == "__main__":
    main()
