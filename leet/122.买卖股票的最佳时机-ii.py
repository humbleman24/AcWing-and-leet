#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [ [0] * len(prices) for i in range(2) ]
        dp[1][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i - 1], dp[1][i-1] + prices[i])
            dp[1][i] = max(dp[1][i - 1], dp[0][i-1] - prices[i])

        return dp[0][len(prices)-1]
# @lc code=end

