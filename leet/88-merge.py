class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] == 0:
                nums1.pop(i)
                m -= 1
            elif nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                i += 1
                j += 1
            else:
                i += 1
        while j < n:
            nums1.append(nums2[j])
            j += 1
        print(nums1)

nums1 = list(map(int,input().split()))
m = int(input())
nums2 = list(map(int,input().split()))
n = int(input())

s = Solution()
s.merge(nums1,m,nums2,n)