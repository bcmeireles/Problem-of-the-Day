[70. Climbing Stairs](https://leetcode.com/problems/minimum-falling-path-sum/description/)

[My submission](https://leetcode.com/problems/minimum-falling-path-sum/submissions/1150234492/)

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Failed miserably when at first I tried to just select the lowest value in the first level and select the lowest possible one to move to from it until the last one. It's not guaranteed that the lowest value of the first value is used to reach the lowest sum.

# Approach
<!-- Describe your approach to solving the problem. -->
- Initialize an auxiliary 2D array `aux` to store intermediate results.
- Initialize the first row of aux with the values from the first row of the input matrix `matrix`.
- Iterate over the remaining rows of matrix. For each element at position `(i, j)`, calculate the minimum falling path sum by considering the three possible paths from the previous row.
- Update the `aux` array with the minimum falling path sum for each position.
- Find the minimum falling path sum in the last `row` of tàe aux array, which represents the overall minimum falling path sum for the entire matrix.

# Complexity
- Time complexity: $$O(n^2)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n^2)$$

<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
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
```