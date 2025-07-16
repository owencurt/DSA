class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        result = []

        for i in range(len(nums)):
            total += nums[i]
            result.append(total)
        return result