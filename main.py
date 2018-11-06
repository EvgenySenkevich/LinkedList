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
        past = self.head

        if node is not None:
            if node.value == val:
                self.head = node.next
                if not all:
                    return

        while node is not None:
            if node.value == val:
                past.next = node.next
                if not all:
                    break
            if node.value != val:
                past = node
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


def sum(first, second):
    first_node = first.head
    second_node = second.head
    sum_arr = LinkedList()

    if first.len() == second.len():
        while first_node is not None:
            sum_arr.add_in_tail(Node(first_node.value+second_node.value))
            first_node = first_node.next
            second_node = second_node.next
        return sum_arr


if __name__ == "__main__":
    pass
