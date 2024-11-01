class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}

        for n in range(len(nums)):
            if nums[n] in comp:
                return [n, comp[nums[n]]]
            
            comp[target-nums[n]] = n

# Two Sum problem in Python for leetcode
