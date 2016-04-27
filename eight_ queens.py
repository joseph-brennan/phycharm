from __future__ import print_function
import unittest

track = False
""" This method assumes the solution is a list of tuples such as:
    [(0, 1), (1, 3), (2, 0), (3, 2)] """


def print_board(solution):

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


def safe((x1, y1), (x2, y2)):
    if x1 == x2:
        return False

    if y1 == y2:
        return False

    if abs(x2 - x1) == abs(y2 - y1):
        return False

    return True


''' solve_queens(row)'''


def solve_queen(row, columns):
    solution = []
    """if the row is greater than the size of the board, we're done"""
    if row > len(solution):
        return solution

    """go through the columns in this row"""
    for columns in row:
        """go through all the already placed queens and see if
            placing a new queen at (row, column) is safe"""

        if safe(queen) is True:
            solution.append(queen)

            """if it is
             place it at (row, column)"""

        else:
            solve_queen(row + 1)

            """if not solve_queens(row+1)
                remove row and column"""


class test_eight_queens(unittest.TestCase):
    def test_safe_empty(self):
        self.assertEqual(safe((None, None), (None, None)), False)
