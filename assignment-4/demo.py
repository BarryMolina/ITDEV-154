from queue import QueueCL
from stack import Stackll
from node import Node


stack = Stackll()
queue = QueueCL()


def display_stack():
    print_stack()
    input("\nPress <Enter> to return to Main Menu ")

def display_queue():
    print_queue()
    input("\nPress <Enter> to return to Main Menu ")

def print_stack():
    print(f"\nStack: {stack}")

def print_queue():
    print(f"\nQueue: {queue}")

def push():
    # loop through generator function
    print_stack()
    data = input("\n\nEnter data to push or press <enter> to stop: ")
    while data:
        node = Node(data)
        stack.push(node)
        print_stack()
        data = input("\n\nEnter data to push or press <enter> to stop: ")

def pop():
    items_remain = True
    print_stack()
    user_input = input("\n\nPress <enter> to pop or 'stop' to stop: ")
    while user_input.lower() != "stop" and items_remain:
        try:
            node = stack.pop()
            print(f"\n\nPopped node: {node.data}")
            print_stack()
            user_input = input("\n\nPress <enter> to pop or 'stop' to stop: ")
        except Exception:
            input("\n\nStack is empty. Press <enter> to return to the Main Menu")
            items_remain = False

def enqueue():
    print_queue()
    data = input("\n\nEnter data to enqueue or press <enter> to stop: ")
    while data:
        node = Node(data)
        queue.enqueue(node)
        print_queue()
        data = input("\n\nEnter data to enqueue or press <enter> to stop: ")

def dequeue():
    items_remain = True
    print_queue()
    user_input = input("\n\nPress <enter> to dequeue or 'stop' to stop: ")
    while user_input.lower() != "stop" and items_remain:
        try:
            node = queue.dequeue()
            print(f"\n\nDequeued node: {node.data}")
            print_queue()
            user_input = input("\n\nPress <enter> to dequeue or 'stop' to stop: ")
        except Exception:
            input("\n\nQueue is empty. Press <enter> to return to the Main Menu")
            items_remain = False


options = [
    display_stack,
    push,
    pop,
    display_queue,
    enqueue,
    dequeue,
]

def main():
    quit = False
    while not quit:
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "Welcome to the StackQueue app.\n"
            "\nPlease select one of the following options:\n"
            "\n--- Stack ---\n"
            "1: Dispay the stack\n"
            "2: Push\n"
            "3: Pop\n"
            "\n--- Queue ---\n"
            "4: Display the queue\n"
            "5: Enqueue\n"
            "6: Dequeue\n"
            "\n0: Quit\n"
        )
        choice = int(input("\n>>> "))
        print()

        if choice == 0:
            quit = True
        else:
            options[choice-1]()


if __name__ == "__main__":
    main()
