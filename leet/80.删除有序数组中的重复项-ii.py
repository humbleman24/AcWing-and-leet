#
# @lc app=leetcode.cn id=80 lang=python
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow, count = 1, 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                count = 1
            elif nums[fast] == nums[slow] and count < 2:
                slow += 1
                nums[slow] = nums[fast]
                count += 1
            fast += 1
        return slow + 1
 
# @lc code=end

