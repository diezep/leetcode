#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for num in nums:
            if target > num:
                index += 1
            else:
                break
        return index
# @lc code=end

