import unittest


class linked_list(object):
    front = rear = None

    current = None  # used in iterator

    class node(object):

        def __init__(self, value, next):
            self.value = value

            self.next = next

    def empty(self):

        return self.front == self.rear == None

    def push_front(self, value):

        if self.empty():

            self.front = self.rear = self.node(value, self.front)

        else:

            x = self.node(value, self.front)

            self.front = x

            if not self.rear:
                self.rear = x

    def pop_front(self):

        if self.empty():
            raise RuntimeError("Empty list duh")

        x = self.front.value

        self.front = self.front.next

        if not self.front:
            self.rear = None

        return x

    @property
    def pop_back(self):

        if self.empty():
            raise RuntimeError("that Empty list")

        ret = self.rear.value

        if self.front == self.rear:  # one element

            self.front = self.rear = None

            return ret

        x = self.front

        while x.next != self.rear:
            x = x.next

        self.rear = x

        return ret

    def push_back(self, value):

        if self.empty():

            self.front = self.rear = self.node(value, None)

        else:

            x = self.node(value, None)

            self.rear.next = x

            self.rear = x

    def __str__(self):
        ret = ""
        x = self.front
        while x != None:
            ret += str(x) + ","
            x = x.next

        self.current = ret
        return self.current

    print current


class test_linked_list(unittest.TestCase):
    def test_none(self):
        self.assertTrue(linked_list().empty())

    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_front())

    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_back)

    def test_push_back_pop_front(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back(2)
        ll.push_back(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_front(), 1)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 3)
        self.assertTrue(ll.empty())

    def test_push_front_pop_front(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_front(), 3)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 1)
        self.assertTrue(ll.empty())

    def test_push_front_pop_back(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back, 1)
        self.assertEquals(ll.pop_back, 2)
        self.assertEquals(ll.pop_back, 3)
        self.assertTrue(ll.empty())

    def test_push_back_pop_back(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back("foo")
        ll.push_back([3, 2, 1])
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back, [3, 2, 1])
        self.assertEquals(ll.pop_back, "foo")
        self.assertEquals(ll.pop_back, 1)
        self.assertTrue(ll.empty())

    def test_push_front(self):
        ll = linked_list()
        self.assertTrue(ll.empty())
        ll.push_front(1)
        self.assertFalse(ll.empty())

    def test_push_back(self):
        ll = linked_list()
        self.assertTrue(ll.empty())
        ll.push_back(1)
        self.assertFalse(ll.empty())


class factorial:
    def fact(self, a):
        if a < 0: raise ValueError("Less than zero")
        if a == 0 or a == 1: return 1

        stack = linked_list()
        while a > 1:
            stack.push_front(a)
            a -= 1

        result = 1
        while not stack.empty():
            result *= stack.pop_front()

        return result


class test_factorial(unittest.TestCase):
    def test_less_than_zero(self):
        self.assertRaises(ValueError, lambda: factorial().fact(-1))

    def test_zero(self):
        self.assertEquals(factorial().fact(0), 1)

    def test_one(self):
        self.assertEquals(factorial().fact(1), 1)

    def test_two(self):
        self.assertEquals(factorial().fact(2), 2)

    def test_10(self):
        self.assertEquals(factorial().fact(10), 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)


if __name__ == "__main__":
    print (factorial().fact(1))
    print (factorial().fact(2))
    print (factorial().fact(100))
