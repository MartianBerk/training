"""
Solution to "Find Zombies" problem on Codewars (Kata 5).
https://www.codewars.com/kata/5464d6811e0c08e574000b76
"""


def find_zombies(matrix):
    """
    Iterate through a matrix of "zombies" where matrix[0][0] is patient zero.
    Anyone matching number to patient zero is infected if connected hortizontally/vertically.
    """
    pz = None
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    infected = [[None for _ in range(matrix_width)] for _ in range(matrix_height)]
    
    def lookback(x, y):
        """
        Lookback through the matrix from a given point.
        Called after an infected is found to backtrace 
        """
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if matrix[i][j] == pz and infected[i][j] != 1:  # base check: number is equal to patient zero & not already infected
                    if j < y and infected[i][j + 1] == 1:  # number to the right of number is also equal to patient zero
                        infected[i][j] = 1
                    elif i < x and infected[i + 1][j] == 1:  # number below number is also equal to patient zero
                        infected[i][j] = 1

    for i, row in enumerate(matrix):
        for j in range(len(row)):
            if i + j == 0:
                pz = matrix[i][j]
                infected[i][j] = 1
            else:
                infected[i][j] = 0
                if matrix[i][j] == pz:  # base check: number is equal to patient zero
                    if j > 0 and infected[i][j - 1] == 1:  # number to the left of number is also equal to patient zero
                        infected[i][j] = 1
                        lookback(i, j)
                    elif i > 0 and infected[i - 1][j] == 1:  # number above number is also equal to patient zero
                        infected[i][j] = 1
                        lookback(i, j)
                        
    return infected