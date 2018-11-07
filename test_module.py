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

    def test_add_in_tail(self):
        a_list = main.LinkedList()
        self.assertIsNone(a_list.head)
        self.assertIsNone(a_list.tail)
        a_list.add_in_tail(main.Node(1))
        self.assertEqual(a_list.head.value, 1)
        a_list.add_in_tail(main.Node(2))
        self.assertEqual(a_list.head.next.value, 2)
        self.assertEqual(a_list.tail.prev.value, 1)

    def test_find(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        self.assertIsNone(a_list.find(3))
        a_list.add_in_tail(main.Node(3))
        self.assertEqual(a_list.find(3).value, 3)

    def test_delete(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        self.assertTrue(self.__check_value(a_list, 2))
        a_list.delete(2)
        self.assertFalse(self.__check_value(a_list, 2))

    def test_add(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        self.assertFalse(self.__check_value(a_list, 4))
        a_list.add(main.Node(4), 2)
        self.assertTrue(self.__check_value(a_list, 4))
        node = a_list.head
        while node is not None:
            if node.value == 4:
                self.assertEqual(node.prev.value, 2)
                self.assertEqual(node.next.value, 3)
            node = node.next

    def test_add_first(self):
        a_list = main.LinkedList()
        a_list.add_in_tail(main.Node(1))
        a_list.add_in_tail(main.Node(2))
        a_list.add_in_tail(main.Node(3))
        self.assertEqual(a_list.head.value, 1)
        a_list.add_first(main.Node(4))
        self.assertEqual(a_list.head.value, 4)
        self.assertEqual(a_list.head.next.value, 1)
        node = a_list.head.next
        self.assertEqual(node.prev.value, 4)


if __name__ == "__main__":
    unittest.main()
