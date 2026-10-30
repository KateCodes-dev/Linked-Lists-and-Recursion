
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        """Insert a node at the beginning in O(1) time."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """Return the sum of node values using recursion."""
        def calculate(node):
            # Base case: an empty remainder has sum zero.
            if node is None:
                return 0

            # Recursive case: current value plus remaining sum.
            return node.data + calculate(node.next)

        return calculate(self.head)

    def recursive_search(self, target):
        """Return True if target is found; otherwise False."""
        def find(node):
            # Base case: reached the end.
            if node is None:
                return False

            # Base case: target found.
            if node.data == target:
                return True

            # Recursive case: search the next node.
            return find(node.next)

        return find(self.head)

    def recursive_reverse(self):
        """Reverse the list in place using recursion."""
        def reverse(node):
            # Base case: empty list or last node.
            if node is None or node.next is None:
                return node

            # Recursively reverse the rest of the list.
            new_head = reverse(node.next)

            # Reverse the link between adjacent nodes.
            node.next.next = node
            node.next = None

            return new_head

        self.head = reverse(self.head)
