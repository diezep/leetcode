#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p0 = 0
        p1 = 0
        best = 0

        st = {}

        while p1 < len(s):
            if not s[p1] in st:
                st[s[p1]] = True
                p1 += 1

            else:
                st.pop(s[p0])
                p0 += 1
            
            if p1 - p0 > best: best = p1 - p0

        return best

# @lc code=end

