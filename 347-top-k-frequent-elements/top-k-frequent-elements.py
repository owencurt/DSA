class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = {}

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            freq_map[num] += 1

        sorted_freq = sorted(freq_map, key=lambda x:freq_map[x], reverse=True)
        return sorted_freq[:k]