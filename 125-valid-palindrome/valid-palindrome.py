class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = [ch.lower() for ch in s if ch.isalnum()]
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
