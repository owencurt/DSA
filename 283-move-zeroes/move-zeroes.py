class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_index], nums[i] = nums[i], nums[insert_index]
                insert_index += 1
        
                