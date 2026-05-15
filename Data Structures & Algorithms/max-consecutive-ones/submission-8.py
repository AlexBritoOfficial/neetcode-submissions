class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0

        for i in range(len(nums)):

            if nums[i] == 1:
                count += 1
            else:
                maximum = max(count,maximum)
                count = 0
        

        return max(count,maximum)