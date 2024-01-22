class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = (len(nums) * (len(nums) + 1)) // 2
        unique = set(nums)
        return [Counter(nums).most_common(1)[0][0], total - sum(unique)]