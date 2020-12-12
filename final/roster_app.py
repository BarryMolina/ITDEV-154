from roster import RosterLL
import orderby as o

employees = [
    ["Barry", "Molina", 27, 100000],
    ["Justin", "Beiber", 25, 50000],
    ["George", "Washington", 350, 1000000]
]

rosterll = RosterLL(nodes=employees)

def display_all():
    allemps = [node for node in rosterll]
    while allemps is not None:
        allemps = display(allemps)



def display(alist):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if not alist:
        input("\n\nThere are no items in this list"
            "\npress <enter> to return to the previous menu\n\n")
        return None

    newlist = None
    print(
            f"   {'First Name':<20}"
            f"{'Last Name':<20}"
            f"{'Age':>10}"
            f"{'Salary':>20}"
            "\n*************************************************************************"
    )
    for i, node in enumerate(alist):
        print(f"{i+1}. {node}")
    print("\n\nSelect one of the following options or"
          "\npress <enter> to return to the previous menu\n\n"
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
                    rosterll.remove_node(alist[num-1].id)
                    alist.pop(num-1)                        # remove item from list
                    newlist = alist
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
                newlist = o.order_by[int(select)-1](alist, asc=True)
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
                newlist = o.order_by[int(select)-1](alist, asc=False)
                break
    return newlist

def add_employee():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\nEnter Employee info or"
        "\npress <enter> at anytime to cancel")
    fname = input("\nFirst Name: ")
    if not fname:
        return
        
    lname = input("\nLast Name: ")
    if not lname:
        return
        
    age = input("\nAge: ")
    if not age:
        return

    salary = input("\nSalary: ")
    if not salary:
        return

    rosterll.add_employee([fname, lname, int(age), int(salary)])

    input("\n\nEmployee added. Press <enter> to return to the Main Menu")


def search_menu():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\nSelect attribute to search by or"
            "\npress <enter> to return to the Main Menu\n\n"
            "1: First Name \n"
            "2: Last Name\n"
            "3: Age\n"
            "4: Salary"
            )
        select = input("\n>>> ")
        if not select:
            break

        if not select.isnumeric or int(select) > 4:
            print("\nInvalid selection")
            continue
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        if select == "1":
            print("\n\nEnter a First Name or"
                "\npress <enter> to return to the Search Menu")
            fname = input("\n>>> ")
            if fname:
                result = rosterll.search_fname(fname)
                while result is not None:
                    result = display(result)
                    
        elif select == "2":
            print("\n\nEnter a Last Name or"
                "\npress <enter> to return to the Search Menu")
            lname = input("\n>>> ")
            if lname:
                result = rosterll.search_lname(lname)
                while result is not None:
                    result = display(result)

        elif select == "3":
            print("\n\nEnter an age or"
                "\npress <enter> to return to the Search Menu")
            age = input("\n>>> ")
            if age:
                result = rosterll.search_age(int(age))
                while result is not None:
                    result = display(result)
                    
        elif select == "4":
            print("\n\nEnter a salary or"
                "\npress <enter> to return to the Search Menu")
            salary = input("\n>>> ")
            if salary:
                result = rosterll.search_salary(int(salary))
                while result is not None:
                    result = display(result)

def filter_menu():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\nSelect attribute to filter by or"
            "\npress <enter> to return to the Main Menu\n\n"
            "1: First Name \n"
            "2: Last Name\n"
            "3: Age\n"
            "4: Salary"
            )
        select = input("\n>>> ")
        if not select:
            break

        if not select.isnumeric or int(select) > 4:
            print("\nInvalid selection")
            continue
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        if select == "1":
            print("\n\nEnter a starting letter or"
                "\npress <enter> to return to the Search Menu")
            char = input("\n>>> ")             
            if char:
                result = rosterll.fname_startswith(char[0])
                while result is not None:
                    result = display(result)

        elif select == "2":
            print("\n\nEnter a starting letter or"
                "\npress <enter> to return to the Search Menu")
            char = input("\n>>> ")             
            if char:
                result = rosterll.lname_startswith(char[0])
                while result is not None:
                    result = display(result)

        elif select == "3":
            while True:
                print("\n\nSelect an option to filter by or"
                    "\npress <enter> to return to the Filter Menu\n\n"
                    "1: Greater than or equal to a given age\n"
                    "2: Less than or equal to a given age\n"
                    )
                select = input("\n>>> ")
                if not select:
                    break
                if not select.isnumeric or int(select) > 2:
                    print("\nInvalid selection")
                elif select == "1":
                    print("\n\nEnter age to filter by or"
                        "\npress <enter> to return to the previous menu")
                    age = input("\n>>> ")             
                    if age:
                        result = rosterll.age_at_or_above(int(age))
                        while result is not None:
                            result = display(result)
                    break

                elif select == "2":
                    print("\n\nEnter age to filter by or"
                        "\npress <enter> to return to the previous menu")
                    age = input("\n>>> ")             
                    if age:
                        result = rosterll.age_at_or_below(int(age))
                        while result is not None:
                            result = display(result)
                    break

        elif select == "4":
            while True:
                print("\n\nSelect an option to filter by or"
                    "\npress <enter> to return to the Filter Menu\n\n"
                    "1: Greater than or equal to a given salary\n"
                    "2: Less than or equal to a given salary\n"
                    )
                select = input("\n>>> ")
                if not select:
                    break
                if not select.isnumeric or int(select) > 2:
                    print("\nInvalid selection")
                elif select == "1":
                    print("\n\nEnter salary to filter by or"
                        "\npress <enter> to return to the previous menu")
                    salary = input("\n>>> ")             
                    if salary:
                        result = rosterll.salary_at_or_above(int(salary))
                        while result is not None:
                            result = display(result)
                    break

                elif select == "2":
                    print("\n\nEnter salary to filter by or"
                        "\npress <enter> to return to the previous menu")
                    salary = input("\n>>> ")             
                    if salary:
                        result = rosterll.salary_at_or_below(int(salary))
                        while result is not None:
                            result = display(result)
                    break

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
        elif choice == 2:
            add_employee()
        elif choice == 3:
            search_menu()
        elif choice == 4:
            filter_menu()

        # else:
        #     options[choice-1](rosterll)


if __name__ == "__main__":
    main()
