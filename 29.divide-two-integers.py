#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = dividend / divisor
        return min(max(int(res), -2**31),  (2**31 - 1))
# @lc code=end

