#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"}":"{", "]":"[", ")":"("}
        s = list(s)

        while s:
            n = s.pop(0)

            if n in ["{", "[", "("]:
                stack.append(n)
                continue

            if not stack or m[n] != stack.pop():
                return False

        return len(stack) == 0
# @lc code=end

