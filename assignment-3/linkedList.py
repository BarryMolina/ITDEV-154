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

    def insert_at(self, pos, data):
        if pos == 1:
            self.insert_beginning(data)
        else:
            p = self.start
            # get node before insertion point
            for x in range(1, pos - 1):
                if p.link is None:
                    break
                p = p.link
            # executes if the loop exited normally
            else:
                temp = Node(data)
                temp.link = p.link
                p.link = temp

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.link

    def delete_last(self):
        if self.start is None:
            return
        # remove only node in list
        elif self.start.link is None:
            self.start = None
        else:
            p = self.start
            # find second to last node
            while p.link.link is not None:
                p = p.link
            p.link = None

    def delete_nth(self, idx):
        if idx == 1:
            self.delete_first()
        else:
            p = self.start
            for x in range(1, idx - 1):
                # if this is the second to last node
                if p.link.link is None:
                    break
                p = p.link
            # loop exits normally
            else:
                p.link = p.link.link

    def reverse(self):
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
        # runs once for each element in list
        while self.start.link is not end:
            p = self.start
            # run up till node before end
            while p.link is not end:
                q = p.link
                if int(p.info) > int(q.info):
                    # python tuple unpacking to swap values
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubble_sort_links(self):
        end = None
        while self.start.link is not end:
            # r contains previous node
            p = r = self.start
            while p.link is not end:
                q = p.link
                if int(p.info) > int(q.info):
                    p.link = q.link
                    q.link = p
                    if p is not self.start:
                        r.link = q
                    else:
                        self.start = q
                    # swap pointers so p continues to reference current node
                    p, q = q, p
                r = p
                p = p.link
            end = p

    def insert_cycle(self, x):
        p = self.start
        px = prev = None
        while p is not None:
            if p.info == x:
                # this node contains x
                px = p
            prev = p
            p = p.link
        if px is not None:
            # set last node to refer to px
            prev.link = px

    def find_cycle(self):
        # list contains at least two nodes
        if (self.start is not None) and (self.start.link is not None):

            slow_p = self.start
            fast_p = self.start

            while (fast_p is not None) and (fast_p.link is not None):
                slow_p = slow_p.link
                fast_p = fast_p.link.link
                if slow_p is fast_p:
                    return slow_p

    def remove_cycle(self):
        # the node at which the slow and fast pointers met
        met_at = self.find_cycle()

        if (met_at is not None):
            p = met_at
            q = met_at
            len_cycle = 0

            # essentially a do-while loop
            while True:
                len_cycle += 1
                q = q.link
                if p == q:
                    break
            len_remaining = 0
            p = self.start
            while p is not q:
                len_remaining += 1
                p = p.link
                q = q.link

            len_list = len_cycle + len_remaining
            p = self.start
            for x in range(1, len_list):
                p = p.link
            p.link = None
