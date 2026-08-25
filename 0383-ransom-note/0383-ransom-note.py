class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        counts = {}
        for ch in magazine:
            if ch not in counts:
                counts[ch] = 1
            else:
                counts[ch] += 1
        for ch in ransomNote:
            if ch not in counts:
                return False

            if counts[ch] == 0:
                return False

            counts[ch] -= 1

        return True