#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        target = 0
        for i in range(len(nums)):
            if count == 0:
                target = nums[i]
                count = 1
            elif nums[i] != target:
                count -= 1
            else:
                count += 1
        return target
# @lc code=end

