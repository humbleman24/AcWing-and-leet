#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        smallest = -1
        biggest = 0
        for i in range(len(prices)):
            if smallest == -1:
                smallest = i
            else:
                if prices[i] < prices[smallest]:
                    smallest = i
            if prices[i] - prices[smallest] > biggest:
                biggest = prices[i] - prices[smallest]
        return biggest
    

    '''
    使用动态规划的话需要两组状态来表示：
    1、止到第i天，在没有持有股票的情况下，最大的利润
    2、止到第i天，持有股票的情况下，最大的"利润"， 或最小的代价
    
    对于第一个数组：
        转移方程为：第i-1天，没有股票；与第i-1天有股票，并在今天卖出
    对于第二个数组：
        转移方程为：第i-1天，没有股票；在第i天买入股票
    
    第二个数组服务于第一个数组的更新，找最小的情况的出现
    '''


        
# @lc code=end

