#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0

        for num in nums2:
            while i < len(nums1) and num > nums1[i]:
                i += 1

            if not i < len(nums1):
                nums1.append(num)
            else:
                nums1.insert(i, num)

        l = len(nums1)
        if l % 2 == 0:
            return (nums1[l // 2] + nums1[(l // 2) - 1]) / 2
        else:
            return nums1[l//2]

# @lc code=end

