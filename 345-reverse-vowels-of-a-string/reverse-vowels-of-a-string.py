class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('AEIOUaeiou')
        s_list = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            elif s[l] and s[r] in vowels:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l, r = l+1, r-1
        return "".join(s_list)
