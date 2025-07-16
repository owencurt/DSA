class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        total = 0
        total = 0
        for account in accounts:
            money = 0
            for i in range(len(account)):
                money += account[i]
            if money > total:
                total = money
        return total

        