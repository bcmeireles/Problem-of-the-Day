class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        aux = [[0] * length for _ in range(length)]

        for i in range(length):
            aux[0][i] = matrix[0][i]

        for i in range(1, length):
            for j in range(length):
                possible = [aux[i - 1][j]]
                if j > 0:
                    possible.append(aux[i - 1][j - 1])
                if j + 1 < length:
                    possible.append(aux[i - 1][j + 1])
                aux[i][j] = min(possible) + matrix[i][j]

        res = math.inf
        for i in range(length):
            res = min(res, aux[length - 1][i])

        return res