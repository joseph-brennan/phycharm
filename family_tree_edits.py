from __future__ import print_function
from sys import stdin
import unittest


class family_tree:
    def __init__(self, init=None):
        self.__value = self.__name = self.__parent = None
        self.__left = self.__right = None

        if init:
            try:
                for i in init:
                    self.add(i[0], i[1])
            except TypeError:
                self.add(init[0], init[0])

    def __iter__(self):
        if self.__left:
            for node in self.__left:
                yield (node)

        yield (self.__value, self.__name)

        if self.__right:
            for node in self.__right:
                yield (node)

    """ Return a preorder list """

    def pre_order(self):
        results = []

        if self.__value is None:
            return results

        results.append((self.__value, self.__name))

        if self.__left:
            results += self.__left.pre_order()

        if self.__right:
            results += self.__right.pre_order()

        # you really should return the results you calculate
        # pass

        return results

    """ Return a in_order list """

    def in_order(self):
        value = self.__value
        results = []

        if value is None:
            return results

        if self.__left:
            results += self.in_order(value)

        # results += [self]

        if self.__right:
            results += self.in_order(value)

    """ Return a post_order list """

    def post_order(self):
        pass

    def __str__(self):
        return ','.join(str(node) for node in self)

    def add(self, value, name):
        if self.__value == self.__left == self.__right == None:
            self.__value = value
            self.__name = name
            self.__parent = None
            return

        if value < self.__value:
            if not self.__left:
                self.__left = family_tree()
                self.__left.__parent = self
                self.__left.__value = value
                self.__left.__name = name
            else:
                self.__left.add(value, name)
        else:
            if not self.__right:
                self.__right = family_tree()
                self.__right.__parent = self
                self.__right.__value = value
                self.__right.__name = name
            else:
                self.__right.add(value, name)

    """ Given a value, return the node with that value. Useful in the
    next two methods """

    def __find(self, value):
        if self.__value == value:
            return self

        if self.__value > value:
            if self.__left:
                return self.__left.__find(value)
            else:
                raise LookupError

        if self.__value < value:
            if self.__right:
                return self.__right.__find(value)
            else:
                raise LookupError

    """ Given a value, return the name of that node's parent """

    def find_parent(self, value):
        return self.__find(value).__parent.__name

        '''
        print(self.__value)
        print(self.__name)
        print(self.__left)
        print(self.__parent)
        print(value)
        if self.__value == value:

            return self.__name

        if self.__parent > value:

            print(value)
            print (self.__name)
            print(self.__parent)
            if self.__left:

                return self.__left.find_parent(value)

            else:

                raise LookupError

        if self.__parent < value:

            if self.__right:

                return self.__right.find_parent(value)

            else:

                raise LookupError
        '''

    """ Given a value, return the name of that node's grand parent """

    def find_grand_parent(self, value):
        pass

    """ Create a list of lists, where each of the inner lists
        is a generation """

    def generations(self):
        """ First, create a list 'this_level' with the root,
                and three empty lists: 'next_level', 'result', and
                'names' """

        """ While 'this_level' has values """
        """ Get the first element and append its name to 'names' """

        """ If the first element has a left, append it to 'next_level'
                Do the same for the right """

        """ If 'this_level' is now empty """
        """ Append 'names' to 'result', set "this_level' to
            'next_level', and 'next_level' and 'names' to empty
             lists """


class test_family_tree(unittest.TestCase):
    """
      20
     /  \
    10  30
       /  \
      25  35
    """

    def setUp(self):
        self.tree = family_tree([(20, "Grandpa"), (10, "Herb"),
                                 (30, "Homer"), (25, "Bart"), (35, "Lisa")])
        self.expected = "(10, 'Herb'),(20, 'Grandpa'),(25, 'Bart'),\
(30, 'Homer'),(35, 'Lisa')"

    '''
    def test_empty(self):
        self.assertEquals(str(family_tree()), '(None, None)')

    def test_add(self):
        bt = family_tree()
        bt.add(20, "Grandpa")
        bt.add(10, "Herb")
        bt.add(30, "Homer")
        bt.add(25, "Bart")
        bt.add(35, "Lisa")
        self.assertEquals(str(bt), self.expected)

    def test_init(self):
        self.assertEquals(str(self.tree), self.expected)

    def test_parent(self):
        self.assertEquals(self.tree.find_parent(35), "Homer")

    def test_grand_parent(self):
        self.assertEquals(self.tree.find_grand_parent(35), "Grandpa")

    def test_generations(self):
        self.assertEquals(self.tree.generations(),
                          [['Grandpa'], ['Herb', 'Homer'], ['Bart', 'Lisa']])
    '''

    """ Write your own tests for inorder etc. here
    used from the discussion board"""

    def test_pre_order(self):
        self.assertEqual((self.tree.pre_order()),
                         [(20, 'Grandpa'), (10, 'Herb'), (30, 'Homer'), (25, 'Bart'), (35, 'Lisa')])

    '''
    def test_post_order(self):
        self.assertEqual((self.tree.post_order()),
                         [(10, 'Herb'), (25, 'Bart'), (35, 'Lisa'), (30, 'Homer'),  (20, 'Grandpa')])

    def test_in_order(self):
        self.assertEquals((self.tree.in_order()), [(10, 'Herb'), (20, 'Grandpa'),
                                                   (25, 'Bart'), (30, 'Homer'), (35, 'Lisa')])
    '''


if '__main__' == __name__:
    """ Read a file with lines of '# name'. Add each to a
    family tree, and print out the resulting generations. """
    ft = family_tree()
    for line in stdin:
        a = line.strip().split(" ")
        ft.add(a[0], a[1])
    print(ft.generations())
