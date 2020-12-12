from roster import LinkedList
import sorter as s

employees = [
    ["Barry", "Molina", 27, 100000],
    ["Justin", "Beiber", 25, 50000],
    ["George", "Washington", 350, 1000000]
]

llist = LinkedList(nodes=employees)

def display_all():
    allemps = [node for node in llist]
    while allemps:
        allemps = display(allemps)



def display(alist):
    newlist = None
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for i, node in enumerate(alist):
        print(f"{i+1}. {node}")
    print("\n\nSelect one of the following options or"
          "\npress <enter> to return to the Main Menu\n\n"
          "1: Remove Employee\n"
          "2: Sort in Ascending Order\n"
          "3: Sort in Descending Order"
          )
    ans = input("\n>>> ")
    if ans == "1":
        while True:
            print("\n\nEnter the line number of employee to remove or"
                  "\npress <enter> to cancel")
            select = input("\n>>> ")
            if not select:
                newlist = alist
                break
            if not select.isnumeric or int(select) > len(alist):
                print("\nInvalid selection")
            else:
                try:
                    num = int(select)
                    llist.remove_node(alist[num-1].id)
                    newlist = [node for node in llist]
                    break
                except Exception as ex:
                    print(f"\n{ex}")
    elif ans == "2":
        while True:
            print("\n\nSelect attribute to sort by or"
                  "\npress <enter> to return to the List Menu\n\n"
                  "1: First Name\n"
                  "2: Last Name\n"
                  "3: Age\n"
                  "4: Salary\n"
                  )
            select = input("\n>>> ")
            if not select:
                newlist = alist
                break
            if not select.isnumeric or int(select) > 4:
                print("\nInvalid selection")
            else:
                newlist = s.sort_by[int(select)-1](alist, asc=True)
                break
    elif ans == "3":
        while True:
            print("\n\nSelect attribute to sort by or"
                  "\npress <enter> to return to the List Menu\n\n"
                  "1: First Name\n"
                  "2: Last Name\n"
                  "3: Age\n"
                  "4: Salary\n"
                  )
            select = input("\n>>> ")
            if not select:
                newlist = alist
                break
            if not select.isnumeric or int(select) > 4:
                print("\nInvalid selection")
            else:
                newlist = s.sort_by[int(select)-1](alist, asc=False)
                break
    return newlist

def main():
    # options = [
    #     display_list,
    # ]
    quit = False
    while not quit:
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "Welcome to the CompanyRoster app.\n"
            "\nPlease select one of the following options:\n"
            "1: Display Roster\n"
            "2: Add Employee\n"
            "3: Search Roster\n"
            "4: Filter Roster\n"
            "\n0: Quit\n"
        )
        choice = int(input("\n>>> "))
        print()

        if choice == 0:
            quit = True
        elif choice == 1:
            display_all()
        # else:
        #     options[choice-1](llist)


if __name__ == "__main__":
    main()
