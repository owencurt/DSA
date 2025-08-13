class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}
        for s in strs:
            s_sorted = tuple(sorted(s))
            if s_sorted in anagram_map:
                anagram_map[s_sorted].append(s)
            else:
                anagram_map[s_sorted] = [s]
        return list(anagram_map.values())