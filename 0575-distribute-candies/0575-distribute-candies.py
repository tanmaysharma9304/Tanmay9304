class Solution(object):
    def distributeCandies(self, candyType):
        total_candies = len(candyType)
        unique_types = len(set(candyType))

        return min(total_candies // 2, unique_types)