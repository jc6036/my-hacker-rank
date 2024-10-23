class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallestNum = nums[0]
        secondNum = smallestNum
        validPair = False

        for i in range(len(nums)):
            #  Both numbers are less than the current and at least one valid pair has been found
            if smallestNum < nums[i] and secondNum < nums[i] and validPair == True:
                return True
            
            #  If we find a new smaller number, save it
            if nums[i] < smallestNum:
                smallestNum = nums[i]
            #  If we find any number greater than the smallest number, save it and say we found a valid pair
            elif nums[i] > smallestNum:
                secondNum = nums[i]
                validPair = True
            
        return False
