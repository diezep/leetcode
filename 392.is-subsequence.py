#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in t:
            if not s:
                break

            if char == s[0]:
                s = s[1:]

        return not bool(s)
# @lc code=end
