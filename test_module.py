import unittest
import main


class LinkTest(unittest.TestCase):

    def test_add_in_tail(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        a_list.add_in_tail(main.Node(4))
        a_list.add_in_tail(main.Node(5))
        node = a_list.head
        i = 1
        while node is not None:
            self.assertEqual(node.value, i)
            node = node.next
            i += 1

    def test_find(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        a_list.add_in_tail(main.Node(4))
        a_list.add_in_tail(main.Node(5))
        self.assertEqual(a_list.find(2).value, 2)

    def test_delete(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        a_list.add_in_tail(main.Node(4))
        a_list.add_in_tail(main.Node(5))
        a_list.delete(1)
        node = a_list.head
        i = 2
        while node is not None:

            self.assertEqual(node.value, i)
            node = node.next
            i += 1

    def test_len(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        a_list.add_in_tail(main.Node(4))
        a_list.add_in_tail(main.Node(5))
        self.assertEqual(a_list.len(), 5)


if __name__ == "__main__":
    unittest.main()
