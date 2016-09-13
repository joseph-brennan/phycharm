from __future__ import print_function
import unittest

track = False
""" This method assumes the solution is a list of tuples such as:
    [(0, 1), (1, 3), (2, 0), (3, 2)] """


class eight_queens:
    def __init__(self, size):
        self.size = size
        self.solutions = []
        self.count = 0

    def print_board(self):
        length = len(self.solutions)

        print("for: ", length)

        if not self.solutions:
            print("No solution found")

        else:
            print(len(self.solutions), "solutions found")

            for solution in self.solutions:
                """keep count of current solution"""
                self.count += 1

                print("solution: ", self.count)

                print('---' * self.size)

                for i in range(self.size):

                    for j in range(self.size):

                        if (i, j) in solution:
                            print(" Q ", end="")

                        else:
                            print(" . ", end="")
                    print()
                print('---' * self.size)

                print("solution", solution)

                print('\n')
        return length

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

    ''' solve_queens(row, tuple)'''
    # placed is a list a tuples where the queens already are

    def solve_queen(self, row, placed):
        if self.size is None:
            return None

        """if track:
            print(row, "row")
            print(placed, "placed")
            print(self.solutions, "found solutions")
            print(len(self.solutions), "number of found solutions")"""

        """if the row is greater than the size of the board, we're done for all possible solutions"""
        if row == self.size:
            self.solutions.append(placed[:])
            if track:
                """this solves for only the first solution and returns from here"""
                return placed

        """go through the columns in this row"""
        for column in range(self.size):
            new_queen = (row, column)

            good = True
            """checking if current queen is safe with the last queen"""
            for queen in placed:
                good &= self.safe(new_queen, queen)

            if good:
                """if it is place it add it to the current list"""
                placed.append(new_queen)

                temp = self.solve_queen(row + 1, placed)

                if not temp:
                    """if not solve_queens(row+1) remove row and column"""
                    placed.remove(new_queen)
                    continue

                return temp


class test_eight_queens(unittest.TestCase):
    def test_solve_queens_empty(self):
        g = eight_queens(None)
        self.assertEqual(g.solve_queen(0, []), None)

    def test_eight_queens_empty(self):
        g = eight_queens(None)
        g.solve_queen(0, [])
        self.assertEqual(g.print_board(), 0)

    def test_eight_queens_two(self):
        g = eight_queens(2)
        g.solve_queen(0, [])
        self.assertEqual(g.print_board(), 0)

    def test_eight_queens_three(self):
        g = eight_queens(3)
        g.solve_queen(0, [])
        self.assertEqual(g.print_board(), 0)

    def test_eight_queens_four(self):
        if not track:
            g = eight_queens(4)
            g.solve_queen(0, [])
            self.assertEqual(g.print_board(), 2)

    def test_eight_queens_eight(self):
        if not track:
            g = eight_queens(8)
            g.solve_queen(0, [])
            self.assertEqual(g.print_board(), 92)

    def test_eight_queens_solve_queens_four(self):
        if track:
            g = eight_queens(4)
            self.assertEqual(g.solve_queen(0, []), [(0, 1), (1, 3), (2, 0), (3, 2)])
            self.assertEqual(g.print_board(), 1)

    def test_eight_queens_solve_queens_eight(self):
        if track:
            g = eight_queens(8)
            self.assertEqual(g.solve_queen(0, []),
                             [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)])

    ''' def test_solve_queen_four(self):
        g = eight_queens(4)
        self.assertEqual(g.solve_queen(0, []), [(0, 1), (1, 3), (2, 0), (3, 2)])

    def test_solve_queen_eight(self):
        g = eight_queens(8)
        self.assertEqual(g.solve_queen(0, []),
                         [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)])
    due to the changes made to what is expected from the solve these no longer are valid '''


if '__main__' == __name__:
    g = eight_queens(8)
    g.solve_queen(0, [])
    g.print_board()
