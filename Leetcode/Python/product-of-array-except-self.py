class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        out.append(1)
        for i in range(len(nums) - 1):
            out.append(nums[i] * out[i])

        product = 1
        n = len(nums) - 1
        out[n] = product * out[n]
        product = product * nums[n]
        n = n - 1
        while n >= 0:
            out[n] = product * out[n]
            product = product * nums[n]
            n = n - 1 
        
        return out
# Answer for leetcode Product of Array Except Self - average runtime, beats 50%
