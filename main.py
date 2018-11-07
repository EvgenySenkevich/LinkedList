class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def delete(self, val):
        node = self.head
        if node is not None:
            if node.value == val:
                self.head = node.next
        while node is not None:
            if node.value == val:
                node = node.prev
                node.next = node.next.next
                break
            node = node.next

    def add(self, node, val):
        main_node = self.head
        while main_node is not None:
            if main_node.value == val:
                node.next = main_node.next
                main_node.next = node
                node.prev = main_node
                break
            main_node = main_node.next

    def add_first(self, node):
        self.head, self.head.next = node, self.head
        self.head.next.prev = self.head

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


if __name__ == "__main__":
    a_list = LinkedList()
    a_list.add_in_tail(Node(1))
    a_list.add_in_tail(Node(2))
    a_list.add_in_tail(Node(3))
    a_list.print_list()
    a_list.add_first(Node(4))
    print()
    a_list.print_list()