class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        seen = {}

        for ch in s:
            if ch not in seen:
                seen[ch] = 1
            else:
                seen[ch] = seen[ch] + 1

        for ch in t:
            if ch not in seen:
                return False

            seen[ch] -= 1

            if seen[ch] < 0:
                return False

        for ch in seen:
            if seen[ch] != 0:
                return False

        return True