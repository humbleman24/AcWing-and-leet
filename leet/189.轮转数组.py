#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 轮转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        num = nums[n-k:n]
        nums[k: n] = nums[:n-k]
        nums[:k] = num
# @lc code=end

