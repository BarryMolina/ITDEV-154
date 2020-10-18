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
        # create new node
        temp = Node(data)
        # insert node in beginning
        temp.link = self.start
        self.start = temp

    def insert_end(self, data):
        temp = Node(data)
        # if list is empty
        if self.start is None:
            self.start = temp
        else:
            p = self.start
            # find last node of list and insert new node
            while p.link is not None:
                p = p.link
            p.link = temp

    def insert_at(self, pos, data):
        # if inserting at beginning
        if pos == 1:
            self.insert_beginning(data)
        else:
            p = self.start
            # try to find node before position
            for x in range(1, pos - 1):
                # if position is not contained in list
                if p.link is None:
                    break
                p = p.link
            # executes if the loop exited normally
            else:
                # insert new node after p
                temp = Node(data)
                temp.link = p.link
                p.link = temp

    def delete_first(self):
        # if list is not empty
        if self.start is not None:
            # remove first element
            self.start = self.start.link

    def delete_last(self):
        # if list is empty
        if self.start is None:
            return
        # else if there is only one node in the list
        elif self.start.link is None:
            # remove it
            self.start = None
        else:
            p = self.start
            # find second to last node of list
            while p.link.link is not None:
                p = p.link
            # delete last node
            p.link = None

    def delete_nth(self, pos):
        if pos == 1:
            self.delete_first()
        else:
            p = self.start
            # find the node before position given
            for x in range(1, pos - 1):
                # if position is out of range
                if p.link.link is None:
                    break
                p = p.link
            # loop exits normally
            else:
                # remove node
                p.link = p.link.link

    def reverse(self):
        # set variables
        prev = None
        p = self.start
        # loop through list
        while p is not None:
            # reference points to previous node
            next = p.link
            p.link = prev
            prev = p
            p = next
        # set start to reference the last, now the first node in the list
        self.start = prev

    def bubble_sort_data(self):
        # set end variable
        end = None
        # while end is not the second node in the list
        while self.start.link is not end:
            p = self.start
            # find largest element and move it to the end
            while p.link is not end:
                q = p.link
                # if p is larger than q
                if int(p.info) > int(q.info):
                    # swap variables
                    p.info, q.info = q.info, p.info
                p = p.link
            # bring end one step closer to start
            end = p

    def bubble_sort_links(self):
        # same as above
        end = None
        while self.start.link is not end:
            # r contains previous node
            p = r = self.start
            while p.link is not end:
                q = p.link
                # if p is larger
                if int(p.info) > int(q.info):
                    # swap references around instead of data
                    p.link = q.link
                    q.link = p
                    # if we're past the beginning of the list
                    if p is not self.start:
                        r.link = q
                    else:
                        # we're at the beginning of the list
                        self.start = q
                    # swap pointers
                    p, q = q, p
                r = p
                p = p.link
            end = p

    def insert_cycle(self, x):
        # set our variables
        p = self.start
        px = prev = None
        # try to find node containing x
        while p is not None:
            # if we find x
            if p.info == x:
                # save it
                px = p
            prev = p
            p = p.link
        # if x was found
        if px is not None:
            # insert loop
            prev.link = px

    def find_cycle(self):
        # if list contains at least two nodes
        if (self.start is not None) and (self.start.link is not None):

            # set up our slow and fast variables
            slow_p = self.start
            fast_p = self.start

            # until we reach the end of the list
            while (fast_p is not None) and (fast_p.link is not None):
                slow_p = slow_p.link
                fast_p = fast_p.link.link
                # slow and fast pointers reference the same node
                if slow_p is fast_p:
                    # return the node at which they met
                    return slow_p

    def remove_cycle(self):
        # figure out if theres a cycle, and if there is where slow and fast meet
        met_at = self.find_cycle()

        # if there is a cycle
        if (met_at is not None):
            # set p and q variables
            p = met_at
            q = met_at
            len_cycle = 0

            # find the lenth of the cycle
            while True:
                len_cycle += 1
                q = q.link
                if p is q:
                    break
            # find the length of list untill loop starts
            len_remaining = 0
            p = self.start
            # advance one step forward to find remaining length
            while p is not q:
                len_remaining += 1
                p = p.link
                q = q.link

            # total list length equals cycle length plus remaining length
            len_list = len_cycle + len_remaining
            p = self.start
            # find last node of list and set it to reference none,
            # removing cycle
            for x in range(1, len_list):
                p = p.link
            p.link = None
