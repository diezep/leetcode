#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min(strs)
        for i in range(len(m)):
            for s in strs:
                if s[i] != m[i]:
                    return m[:i]
        return m
# @lc code=end

