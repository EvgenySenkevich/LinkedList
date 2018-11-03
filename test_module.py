import unittest
import main


class LinkTest(unittest.TestCase):

    def __check_value(self, a_list, val):
        node = a_list.head
        while node is not None:
            if node.value == val:
                return True
            node = node.next
        return False

    def test_node_none(self):
        node = main.Node(5)
        self.assertEqual(node.value, 5)
        self.assertIsNone(node.next)

    def test_none(self):
        a_list = main.LinkedList()
        self.assertIsNone(a_list.head)
        self.assertIsNone(a_list.tail)

    def test_add_in_tail(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        a_list.add_in_tail(main.Node(4))
        a_list.add_in_tail(main.Node(5))
        self.assertFalse(self.__check_value(a_list, 6))
        a_list.add_in_tail(main.Node(6))
        self.assertTrue(self.__check_value(a_list, 6))

    def test_find(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        a_list.add_in_tail(main.Node(4))
        a_list.add_in_tail(main.Node(5))
        self.assertTrue(self.__check_value(a_list, 2))
        self.assertEqual(a_list.find(2).value, 2)

    def test_delete(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        a_list.add_in_tail(main.Node(4))
        a_list.add_in_tail(main.Node(5))
        self.assertTrue(self.__check_value(a_list, 1))
        a_list.delete(1)
        self.assertFalse(self.__check_value(a_list, 1))

    def test_len(self):
        a_list = main.LinkedList()
        self.assertEqual(a_list.len(), 0)
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        a_list.add_in_tail(main.Node(4))
        a_list.add_in_tail(main.Node(5))
        self.assertEqual(a_list.len(), 5)


if __name__ == "__main__":
    unittest.main()
