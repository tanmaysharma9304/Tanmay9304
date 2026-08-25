class Solution(object):
    def frequencySort(self, s):
        count = {}

        # Frequency count
        for ch in s:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1

        # Sort characters by frequency (highest first)
        sorted_counts = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Build answer
        ans = ""

        for ch, freq in sorted_counts:
            ans += ch * freq

        return ans