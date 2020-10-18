from node import Node

class QueueCL:
    def __init__(self):
        self.end = None

    # object representation
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        return f"[{', '.join(nodes)}]"

    def __iter__(self):
        # if list is empty
        if not self.end:
            return
        # create new node set to start of list
        node = self.end.next
        # cycle through nodes
        while True:
            yield node
            node = node.next
            # once start node has been reached again
            if node == self.end.next:
                break

    # add new node at the end of the list
    def enqueue(self, node):
        # if the list is empty
        if not self.end:
            # set end to new node
            self.end = node
            # point end node at itself
            self.end.next = self.end
        else:
            # point new node at start node
            node.next = self.end.next
            # point end node at the new node
            self.end.next = node
            # end now refers to the new node
            self.end = node

    # remove node from the beginning of the list
    def dequeue(self):
        # if the queue is empty
        if not self.end:
            raise Exception("Queue is empty")
        # if the list only has one node (last node points at itself)
        if self.end.next == self.end:
            # store the end node in a new variable
            node = self.end
            # delete the node
            self.end = None
        else:
            # store last node in a new variable
            node = self.end.next
            # point the last node at the one two nodes ahead (deletes first)
            self.end.next = node.next

        return node
