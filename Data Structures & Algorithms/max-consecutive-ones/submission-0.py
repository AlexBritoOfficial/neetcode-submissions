class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max = 0

        for i in range(len(nums)):

            if nums[i] == 1:
                count += 1
            else:

                if count > max:
                    max = count
                count = 0
        if count > max:
            max = count

        return max