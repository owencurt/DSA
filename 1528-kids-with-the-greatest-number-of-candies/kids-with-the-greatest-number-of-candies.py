class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        result = []
        greatest = max(candies)
        for candy in candies:
            val = candy + extraCandies
            if val >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result