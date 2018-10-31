import unittest
import main


class LinkTest(unittest.TestCase):
    a_list = main.LinkedList()
    a_list.add_in_tail(main.Node(1))
    a_list.add_in_tail(main.Node(2))
    a_list.add_in_tail(main.Node(3))
    a_list.add_in_tail(main.Node(4))
    a_list.add_in_tail(main.Node(5))

    def test_add_in_tail(self):
        node = self.a_list.head
        i = 1
        while node is not None:
            self.assertEqual(node.value, i)
            node = node.next
            i += 1

    def test_find(self):
        self.assertEqual(self.a_list.find(2).value, 2)

    def test_delete(self):
        self.a_list.delete(1)
        node = self.a_list.head
        i = 2
        while node is not None:
            self.assertEqual(node.value, i)
            node = node.next
            i += 1


if __name__ == "__main__":
    unittest.main()
