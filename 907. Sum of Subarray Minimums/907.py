class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def monostack(arr):
            stack = []
            result = [0 for x in arr]

            for i in range(len(arr)):
                while stack and arr[i] < arr[stack[-1]]:
                    j = stack.pop()
                    k = stack[-1] if stack else -1
                    result[j] = arr[j] * (i - j) * (j - k)

                stack.append(i)

            while stack:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result[j] = arr[j] * (len(arr) - j) * (j - k)

            return result

        result = monostack(arr)

        return sum(result) % (10**9 + 7)