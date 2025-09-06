#
# @lc app=leetcode id=2129 lang=python3
#
# [2129] Capitalize the Title
#

# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join(map(lambda t: t if len(t) <= 2 else t.title(), title.lower().split()))

# @lc code=end
