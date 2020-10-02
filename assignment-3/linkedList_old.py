class Node:
    def __init__(self, info):
        self.info = info
        self.link = None


class LinkedList:
    def __init__(self):
        self.start = None

    def clear(self):
        self.start = None

    def populate(self, items):
        for item in items:
            self.insert_end(item)

    # generator function
    def get_list(self):
        p = self.start
        while p is not None:
            yield p.info
            p = p.link

    def display_numbered_list(self):
        count = 1
        p = self.start
        while p is not None:
            print(str(count) + ". " + str(p.info))
            count += 1
            p = p.link

    def num_items(self):
        count = 0
        p = self.start
        while p is not None:
            count += 1
            p = p.link
        return count

    def insert_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
        else:
            p = self.start
            while p.link is not None:
                p = p.link
            p.link = temp

    def insert_after(self, node_info, data):
        p = self.start
        while p is not None:
            if p.info == node_info:
                temp = Node(data)
                temp.link = p.link
                p.link = temp
                break
            p = p.link
        else:
            print("node with data " + str(node_info) + " not found")

    def insert_before(self, node_info, data):
        if self.start is None:
            print("list is emply")
        elif self.start.info == node_info:
            self.insert_beginning(data)
        else:
            p = self.start
            while p.link is not None:
                if p.link.info == node_info:
                    temp = Node(data)
                    temp.link = p.link
                    p.link = temp
                    break
                p = p.link
            else:
                print("node with data " + str(node_info) + " not found")

    def insert_at(self, idx, data):
        if idx == 1:
            self.insert_beginning(data)
        else:
            p = self.start
            for x in range(1, idx - 1):
                if p.link is None:
                    print("You can only insert up through node " + str(x))
                    break
                p = p.link
            else:
                temp = Node(data)
                temp.link = p.link
                p.link = temp

    def insert_at_while(self, idx, data):
        if idx == 1:
            self.insert_beginning(data)
        else:
            p = self.start
            node_idx = 1
            while (node_idx < idx - 1) and (p.link is not None):
                p = p.link
                node_idx += 1
            if p.link is None:
                print("index out of bounds")
            else:
                temp = Node(data)
                temp.link = p.link
                p.link = temp

    def delete_first_node(self):
        if self.start is not None:
            self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return
        elif self.start.link is None:
            self.start = None
        else:
            p = self.start
            while p.link.link is not None:
                p = p.link
            p.link = None

    # delete node containing value
    def delete_node(self, value):
        if self.start is None:
            print("List is empty")
        elif self.start.info == value:
            self.start = self.start.link
        else:
            p = self.start
            while p.link is not None:
                if p.link.info == value:
                    break
                p = p.link
            if p.link is None:
                print("Element " + str(value) + " not in list")
            else:
                p.link = p.link.link

    def delete_at(self, idx):
        if idx == 1:
            self.delete_first_node()
        else:
            p = self.start
            for x in range(1, idx - 1):
                if p.link.link is None:
                    print("You can only delete up through node " + str(x + 1))
                    break
                p = p.link
            else:
                p.link = p.link.link

    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubble_sort_data(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if int(p.info) > int(q.info):
                    temp = p.info
                    p.info = q.info
                    q.info = temp
                p = p.link
            end = p

    def bubble_sort_links(self):
        end = None
        while end != self.start.link:
            p, r = self.start
            while p.link != end:
                q = p.link
                if int(p.info) > int(q.info):
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    temp = p
                    p = q
                    q = temp


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
        size = int(input("\nEnter number of items to input: "))
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
    list.delete_first_node()


@show_old_new
def remove_last(list):
    list.delete_last_node()


@show_old_new
def remove_nth_position(list):
    idx = int(input("\nEnter position of element to be deleted: "))
    list.delete_at(idx)


@show_old_new
def reverse(list):
    list.reverse_list()


@show_old_new
def sort_data(list):
    list.bubble_sort_data()


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
    sort_data
]

def main_menu():
    my_list = LinkedList()
    create_list(my_list, [4, 1, 8, 3, 0, 9, 2])

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
            "10: Bubble sort by exchanging data"
        )

        choice = int(input("\n>>> "))
        print()

        options[choice-1](my_list)

        input("\nPress <Enter> to return to Main Menu ")


def main():
    main_menu()


if __name__ == "__main__":
    main()
