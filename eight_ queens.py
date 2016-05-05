from __future__ import print_function
import unittest

track = True
""" This method assumes the solution is a list of tuples such as:
    [(0, 1), (1, 3), (2, 0), (3, 2)] """


class eight_queens:
    def __init__(self, size):
        self.size = size
        self.solution = []

    def print_board(self, solution):

        length = len(solution)

        print("for:", length)

        print('-' * length)

        if not solution:

            print("no solution found")
        else:
            for i in range(length):

                for j in range(length):

                    if (i, j) in solution:

                        print("Q", end="")
                    else:

                        print(".", end="")
                print()

        print('-' * length)

    ''' Given the location of two queens, find if they are safe
        from each other. '''

    def safe(self, (x1, y1), (x2, y2)):
        if x1 == x2:
            return False

        if y1 == y2:
            return False

        if abs(x2 - x1) == abs(y2 - y1):
            return False

        return True

    ''' solve_queens(row)'''
    # placed is a list a tuples where the queens already are

    def solve_queen(self, row, placed):
        current = placed
        pre_queen = (0, 0)

        if track:
            print(row, "row")
            print(placed, "placed")
            print(pre_queen, "pre queen")

        """if the row is greater than the size of the board, we're done"""
        if row > self.size:
            self.solution = current
            # self.print_board(self.solution)
            return self.solution

        """go through the columns in this row"""
        for column in range(self.size):
            new_queen = (row, column)
            """go through all the already placed queens and see if
                placing a new queen at (row, column) is safe"""

            if self.safe(new_queen, pre_queen) is True:
                current.append(new_queen)
                pre_queen = new_queen
                self.solve_queen(row + 1, current)

                """if it is
                 place it at (row, column)"""

            if not self.solve_queen(row + 1, current):
                continue

            """if not solve_queens(row+1)
                 remove row and column"""

        for queen in current:
            if self.safe(queen, new_queen) is True:
                continue

            else:
                current.remove(queen)
                self.solve_queen(row, current)


class test_eight_queens(unittest.TestCase):
    def test_solve_queen(self):
        g = eight_queens(4)
        self.assertEqual(g.solve_queen(0, [(0, 1), (1, 3), (2, 0)]), [(0, 1), (1, 3), (2, 0), (3, 2)])

