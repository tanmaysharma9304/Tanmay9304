class Solution:
    def finalString(self, s):
        new = ""

        for ch in s:
            if ch == "i":
                new = new[::-1]
            else:
                new = new + ch

        return new