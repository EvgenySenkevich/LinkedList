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

    def find(self, val, all = False):
        if not all:
            node = self.head
            while node is not None:
                if node.value == val:
                    return node
                node = node.next
            return None
        else:
            arr = []
            node = self.head
            while node is not None:
                if node.value == val:
                    arr.append(node)
                node = node.next
            return arr

    def delete(self, val, all=False):
        if not all:
            node = self.head
            past_node = self.head

            while node is not None:
                if self.head.value == val:
                    self.head = node.next
                    break
                elif node.value == val:
                    past_node.next = node.next
                    break
                past_node = node
                node = node.next
        else:
            node = self.head
            past_node = self.head

            while node is not None:
                if self.head.value == val:
                    self.head = node.next
                if node.value == val:
                    past_node.next = node.next
                past_node = node
                node = node.next

    def clear(self):
        self.head = None
        self.tail = None

    def add(self, num, val):
        node = self.head
        i = 0
        while node is not None:
            if i == num:
                val.next = node.next
                node.next = val
            i += 1
            node = node.next

    def len(self):
        node = self.head
        i = 0
        while node is not None:
            node = node.next
            i += 1
        return i

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next


if __name__ == "__main__":
    l_list = LinkedList()
    l_list.add_in_tail(Node(1))
    l_list.add_in_tail(Node(2))
    l_list.add_in_tail(Node(4))
    l_list.add_in_tail(Node(2))
    l_list.add_in_tail(Node(2))
    l_list.add_in_tail(Node(4))

    l_list.print_all_nodes()
    print()
    l_list.delete(2, all=True)
    l_list.print_all_nodes()

