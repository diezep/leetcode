#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        if not word:
            self.is_end = True
            return

        char = word[0]
        if char not in self.children:
            self.children[char] = WordDictionary()
        self.children[char].addWord(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.is_end

        char = word[0]
        if char == ".":
            for child in self.children:
                if self.children[child].search(word[1:]):
                    return True
        
        elif char in self.children:
            if self.children[char].search(word[1:]):
                return True

        return False

        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad"))
# print(obj.search("bad"))
# print(obj.search(".ad"))
# print(obj.search("b.."))
# @lc code=end

