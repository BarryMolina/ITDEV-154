from linkedlist import LinkedList

def show_old_new(func):
    def wrapper_old_new(list):
        print("\nOld List:", end=" ")
        display_list(list)
        func(list)
        print("\nNew List:", end=" ")
        display_list(list)
    return wrapper_old_new


def create_list(list, items=None):
    list.clear()
    if items:
        list.populate(items)
    else:
        size = int(input("Enter number of items to input: "))
        for x in range(size):
            list.insert_end(input("Enter list item: "))


def display_list(list):
    # loop through generator function
    for x in list.get_list():
        print(x, end=" ")
    print()


@show_old_new
def add_beginning(list):
    data = input("\nEnter data to add: ")
    list.insert_beginning(data)


@show_old_new
def add_end(list):
    data = input("\nEnter data to add: ")
    list.insert_end(data)


@show_old_new
def add_nth_position(list):
    idx = int(input("\nEnter position of element to be inserted: "))
    data = input("Data to add: ")
    list.insert_at(idx, data)


@show_old_new
def remove_first(list):
    list.delete_first()


@show_old_new
def remove_last(list):
    list.delete_last()


@show_old_new
def remove_nth_position(list):
    idx = int(input("\nEnter position of element to be deleted: "))
    list.delete_nth(idx)


@show_old_new
def reverse(list):
    list.reverse()


@show_old_new
def sort_data(list):
    try:
        list.bubble_sort_data()
    except ValueError:
        print("\nUnable to sort list containing strings")


@show_old_new
def sort_links(list):
    try:
        list.bubble_sort_links()
    except ValueError:
        print("\nUnable to sort list containing strings")


def insert_cycle(list):
    print("\nList:", end=" ")
    display_list(list)
    cycle_start = input("\nEnter value of node where cycle will be inserted: ")
    list.insert_cycle(cycle_start)

def detect_cycle(list):
    if list.find_cycle() is None:
        print("\nNo cycle detected")
    else:
        print("\nCycle detected")

def remove_cycle(list):
    if list.find_cycle() is None:
        print("\nNo cycle detected")
    else:
        print("\nCycle detected")
        list.remove_cycle()
        print("\nCycle removed")
        print("\nNew List:", end=" ")
        display_list(list)


options = [
    create_list,
    display_list,
    add_beginning,
    add_end,
    add_nth_position,
    remove_first,
    remove_last,
    remove_nth_position,
    reverse,
    sort_data,
    sort_links,
    insert_cycle,
    detect_cycle,
    remove_cycle
]

def main():
    my_list = LinkedList()
    create_list(my_list, ["4", "1", "8", "3", "0", "9", "2"])

    while True:
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "Welcome to the LinkedList app.\n"
            "\nPlease select one of the following options:\n\n"
            "1: Create new single linked list\n"
            "2: Display list\n"
            "3: Add element at beginning of list\n"
            "4: Add element at end of list\n"
            "5: Add element at nth position\n"
            "6: Remove element at beginning of list\n"
            "7: Remove element at end of list\n"
            "8: Remove element at nth position\n"
            "9: Reverse the list\n"
            "10: Bubble sort by exchanging data\n"
            "11: Bubble sort by exchanging links\n"
            "12: Insert cycle\n"
            "13: Detect cycle\n"
            "14: Remove cycle"
        )
        choice = int(input("\n>>> "))
        print()

        options[choice-1](my_list)

        input("\nPress <Enter> to return to Main Menu ")


if __name__ == "__main__":
    main()
