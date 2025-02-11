class CircularList:
    class Node():
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self):
        self.size = 0
        self.curr = None

    def get(self, i: int = 0):
        """
        Get the value of the node `i` positions from the current position.

        `i`: steps from the current position (positive for clockwise, negative for anti-clockwise)
        """
        if self.curr is None:
            raise IndexError("List is empty!")
        curr = self.curr
        for _ in range(i):
            curr = self.curr
        return curr.value

    def insert(self, value, i: int = 0):
        """
        Insert a new `value` node `i` positions from the current position. The current position is updated to the
        inserted node.

        `value`: the new value to insert
        `i`:     steps from the current position (positive for clockwise, negative for anti-clockwise)
        """
        self.size += 1
        if self.curr is None:
            self.curr = self.Node(value)
            self.curr.next = self.curr
            self.curr.prev = self.curr
            return
        for _ in range(abs(i)):
            self.curr = self.curr.next if i > 0 else self.curr.prev
        node = self.Node(value, self.curr, self.curr.next)
        self.curr.next.prev = node
        self.curr.next = node
        self.curr = node

    def pop(self, i: int = 0):
        """
        Remove the node `i` positions from the current position and return its value. The current position is updated
        to the node clockwise from the removed node.

        `i`:     steps from the current position (positive for clockwise, negative for anti-clockwise)
        """
        if self.curr is None:
            raise IndexError("List is empty!")
        self.size -= 1
        if self.size == 0:
            v = self.curr.value
            self.curr = None
            return v
        for _ in range(abs(i)):
            self.curr = self.curr.next if i > 0 else self.curr.prev
        v = self.curr.value
        self.curr.next.prev = self.curr.prev
        self.curr = self.curr.next
        self.curr.prev.next = self.curr
        return v
