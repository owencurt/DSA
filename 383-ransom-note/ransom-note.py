class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_dict = {}
        for ch in magazine:
            if ch in mag_dict:
                mag_dict[ch] += 1
            else:
                mag_dict[ch] = 1
        for ch in ransomNote:
            if ch in mag_dict:
                mag_dict[ch] -= 1
                if mag_dict[ch] < 0:
                    return False
            else:
                return False
        return True