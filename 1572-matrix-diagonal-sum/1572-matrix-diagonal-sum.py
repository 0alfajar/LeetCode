class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        main_diagonal = [mat[i][i] for i in range(n)]
        anti_diagonal = [mat[i][n - 1 - i] for i in range(n)]

        if n % 2 == 1:
           anti_diagonal.pop(len(anti_diagonal)//2)

        return sum(main_diagonal) + sum(anti_diagonal)