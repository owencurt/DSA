class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        area = 0

        while l < r:
            temp = min(height[l], height[r]) * (r - l)
            area = max(area, temp)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return area