class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        index = 0

        shorter = min(len(word1), len(word2))
        for i in range(shorter):
            result += word1[i]
            result += word2[i]
            index += 1
        result += word2[index:]
        result += word1[index:]
        return result