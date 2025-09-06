#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        s = list(s)
        while s:
            if ''.join(s[:2]) in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                tmp = ''.join(s[:2])
                s = s[2:]

                if tmp == "CM": total += 900
                elif tmp == "CD": total += 400
                elif tmp == "XC": total += 90
                elif tmp == "XL": total += 40
                elif tmp == "IX": total += 9
                elif tmp == "IV": total += 4

            else:
                tmp = s.pop(0)
                if tmp == "I": total += 1
                elif tmp == "V": total += 5
                elif tmp == "X": total += 10
                elif tmp == "L": total += 50
                elif tmp == "C": total += 100
                elif tmp == "D": total += 500
                elif tmp == "M": total += 1000
        
        return total
# @lc code=end

