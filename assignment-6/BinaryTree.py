class Node():
    def __init__(self, info):
        self.left_child = None
        self.right_child = None
        self.info = info


class BinarySearchTree():
    def __init__(self, values=None):
        self.root = None
        if values:
            self.insert_many(values)

    def __iter__(self):
        def inorder(p):
            if p is None:
                return
            yield from inorder(p.left_child)
            yield p
            yield from inorder(p.right_child)

        yield from inorder(self.root)

    def __repr__(self):
        tree = ""
        for node in self:
            tree += f"{node.info} "
        return tree

    def insert(self, x):
        p = self.root
        par = None

        while p is not None:
            par = p
            if x < p.info:
                p = p.left_child
            elif x > p.info:
                p = p.right_child
            else:
                raise Exception(f"{x} is already present in the tree")

        temp = Node(x)

        if par is None:
            self.root = temp
        elif x < par.info:
            par.left_child = temp
        else:
            par.right_child = temp

    def insert_many(self, values):
        for value in values:
            self.insert(value)

    def delete(self, x):
        p = self.root
        par = None

        # find node with p.info == x
        while p is not None:
            if x == p.info:
                break
            par = p
            if x < p.info:
                p = p.left_child
            else:
                p = p.right_child
        if p is None:
            raise Exception(f"Node with value {x} not found")

        # If node has two children
        # Copy value of inorder successor to node to be deleted
        if p.left_child is not None and p.right_child is not None:
            ps = p
            s = p.right_child

            while s.left_child is not None:
                ps = s
                s = s.left_child
            p.info = s.info
            p = s
            par = ps

        # Node has either 1 child or no children
        if p.left_child is not None:
            child = p.left_child
        else:
            child = p.right_child

        # if node to be deleted is the root node
        if par is None:
            self.root = child
        # p is left child
        elif p == par.left_child:
            par.left_child = child
        # p is right child
        else:
            par.right_child = child


def display_tree(tree):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Binary Search Tree: ")
    print(tree)
    input("\n\n Press <enter> to return to the Main Menu")


def insert_node(tree):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"\nCurrent tree: \n{tree}")
    while True:
        print("\n\nEnter a value to insert or"
                "\npress <enter> to return to the Main Menu")

        ans = input("\n>>> ")
        if not ans:
            break

        try:
            num = int(ans)
            tree.insert(num)
            print(f"\n{num} inserted in tree.")
        except Exception as ex:
            print(f"\n{ex}")
        finally:
            print(f"\nCurrent tree: \n{tree}")



def delete_node(tree):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"\nCurrent tree: \n{tree}")
    while True:
        print("\n\nEnter a value to delete or"
                "\npress <enter> to return to the Main Menu")

        ans = input("\n>>> ")
        if not ans:
            break

        try:
            num = int(ans)
            tree.delete(num)
            print(f"\n{num} deleted from tree.")
        except Exception as ex:
            print(f"\n{ex}")
        finally:
            print(f"\nCurrent tree: \n{tree}")


options = [
    display_tree,
    insert_node,
    delete_node,
]

def main():
    tree = BinarySearchTree([4, 8, 1, 0, 9])
    quit = False
    while not quit:
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "Welcome to the BinarySearchTree app.\n"
            "\nPlease select one of the following options:\n"
            "1: Display Tree\n"
            "2: Insert Node\n"
            "3: Delete Node\n"
            "\n0: Quit\n"
        )
        choice = int(input("\n>>> "))
        print()

        if choice == 0:
            quit = True
        else:
            options[choice-1](tree)


if __name__ == "__main__":
    main()
