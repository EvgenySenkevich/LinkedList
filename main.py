class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            if self.head is self.find(val):
                self.head = self.find(val).next
                break
            elif node.next is self.find(val):
                node.next = self.find(val).next
                break
            node = node.next

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next


if __name__ == "__main__":
    l_list = LinkedList()
    l_list.add_in_tail(Node(4))
    l_list.add_in_tail(Node(2))
    l_list.add_in_tail(Node(8))
    l_list.add_in_tail(Node(9))
    l_list.print_all_nodes()

    print()
    l_list.delete(4)
    l_list.delete(2)
    l_list.print_all_nodes()
