class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        
        if l == 0:
            return 0
        
        if l == 1:
            return nums[0]

        prev_max = 0
        curr_max = 0

        for i in range(l):
            new_max = max(prev_max + nums[i], curr_max)
            prev_max = curr_max
            curr_max = new_max

        return curr_max