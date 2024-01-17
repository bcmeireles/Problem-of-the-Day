class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = []
        for x in set(arr):
            count = arr.count(x)
            if count in counts:
                return False
            counts.append(count)
        return True