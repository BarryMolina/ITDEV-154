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
            f"{self.fname:.<20}"
            f"{self.lname:.<20}"
            f"{self.age:.>10}"
            f"{self.salary:.>20,}"
            # f"{self.id:4}"
        )

class RosterLL:
    def __init__(self, nodes=None):
        # a unique id for each node
        self.counter = 1
        self.head = None

        # pre-load linked list from nodes
        if nodes is not None:
            data = nodes.pop(0)
            node = Node(self.counter, *data)
            self.counter += 1
            self.head = node
            for elem in nodes:
                node.next = Node(self.counter, *elem)
                self.counter += 1
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_employee(self, data):
        node = Node(self.counter, *data)    # unpack values in data list
        if not self.head:
            self.head = node
            return
        for current_node in self:           # get to end of list
            pass
        current_node.next = node            # add new node

        self.counter += 1                   # increment counter


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

    # search methods
    def search_fname(self, fname):
        results = []
        node = self.head
        for node in self:
            if node.fname == fname:
                results.append(node)
        return results

    def search_lname(self, lname):
        results = []
        node = self.head
        for node in self:
            if node.lname == lname:
                results.append(node)
        return results

    def search_age(self, age):
        results = []
        node = self.head
        for node in self:
            if node.age == age:
                results.append(node)
        return results

    def search_salary(self, salary):
        results = []
        node = self.head
        for node in self:
            if node.salary == salary:
                results.append(node)
        return results
    
    # filter methods
    def fname_startswith(self, letter):
        subList = []
        node = self.head
        for node in self:
            if node.fname.startswith(letter):
                subList.append(node)
        return subList

    def lname_startswith(self, letter):
        subList = []
        node = self.head
        for node in self:
            if node.lname.startswith(letter):
                subList.append(node)
        return subList

    def age_at_or_above(self, age):
        subList = []
        node = self.head
        for node in self:
            if node.age >= age:
                subList.append(node)
            node = node.next
        return subList
    def age_at_or_below(self, age):
        subList = []
        node = self.head
        for node in self:
            if node.age <= age:
                subList.append(node)
        return subList
    def salary_at_or_above(self, salary):
        subList = []
        node = self.head
        for node in self:
            if node.salary >= salary:
                subList.append(node)
        return subList
    def salary_at_or_below(self, salary):
        subList = []
        node = self.head
        for node in self:
            if node.salary <= salary:
                subList.append(node)
        return subList

