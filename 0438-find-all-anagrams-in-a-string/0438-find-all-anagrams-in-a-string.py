class Solution:
    def findAnagrams(self, s, p):

        p_count = {}
        window = {}
        ans = []
        for ch in p:
            if ch not in p_count:
                p_count[ch] = 1
            else:
                p_count[ch] += 1

        left = 0

        for right in range(len(s)):

            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1

            if right - left + 1 > len(p):

                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            if window == p_count:
                ans.append(left)

        return ans