class Solution:
    def maximumWealth(self, accounts):
        
        max_sum = 0

        for i in range(len(accounts)):
            
            total = 0

            for j in range(len(accounts[i])):
                total = total + accounts[i][j]

            if total > max_sum:
                max_sum = total

        return max_sum