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

    def find(self, val, all=False):
        arr = []
        node = self.head

        while node is not None:
            if node.value == val:
                if not all:
                    return node
                arr.append(node)
            node = node.next
        return arr

    def delete(self, val, all=False):
        node = self.head

        if node is not None:
            if node.value == val:
                self.head = node.next
                return

        while node is not None:
            if node.value == val:
                break
            past = node
            node = node.next

        past.next = node.next

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
    l_list.add_in_tail(Node(3))

    l_list.print_all_nodes()
    print()
    
    l_list.delete(2, all=True)
    l_list.print_all_nodes()

