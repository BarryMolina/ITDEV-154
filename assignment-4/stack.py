from node import Node

class Stackll:
    def __init__(self):
        self.head = None

    # object representation
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        return f"[{', '.join(nodes)}]"

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # add node to beginning of list
    def push(self, node):
        # sets nodes next value to the start of linked list
        node.next = self.head
        # sets the start of the linked list to point at the new node
        self.head = node

    # removes the first node and returns it
    def pop(self):
        # if the list is empty
        if not self.head:
            raise Exception("Stack is empty")
        # otherwise set a new node variable equal to the first node
        node = self.head
        # delete the first node in the list
        self.head = self.head.next

        return node
