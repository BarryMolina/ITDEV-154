class Node:
    def __init__(self, node_id, fname, lname, age, salary):
        self.id = node_id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.salary = salary
        self.next = None

    def __repr__(self):
        return (
            f'{self.fname:.<20}'
            f'{self.lname:.<20}'
            f'{self.age:.>10}'
            f'{self.salary:.>20,}'
            f'{self.id:4}'
        )

class LinkedList:
    def __init__(self, nodes=None):
        self.counter = 1
        self.head = None
        if nodes is not None:
            data = nodes.pop(0)
            node = Node(self.counter, *data)
            self.counter += 1
            self.head = node
            for elem in nodes:
                node.next = Node(self.counter, *elem)
                self.counter += 1
                node = node.next

    # object representation
    # def __repr__(self):
    #     node = self.head
    #     nodes = []
    #     while node is not None:
    #         nodes.append(repr(node))
    #         node = node.next
    #     nodes.append("None")
    #     return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data '{target_node_data}' not found")

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")

    def remove_node(self, target_node_id):
        if not self.head:
            raise Exception("List is empty")

        if self.head.id == target_node_id:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.id == target_node_id:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node not found")
