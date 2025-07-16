class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left = (i == 0 or flowerbed[i-1] == 0)
                empty_right = (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)
                if empty_left and empty_right:
                    count += 1
                    flowerbed[i] = 1
        return count >= n