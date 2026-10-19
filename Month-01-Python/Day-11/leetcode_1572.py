class Solution:
    def diagonalSum(delf, mat):
        n = len(mat)
        total = 0

        for i in range(n):
            total = total + mat[i][i]
            total = total + mat[i][n - 1 - i]

        if n % 2 != 0:
            total = total -mat[n // 2][n // 2]

        return total
