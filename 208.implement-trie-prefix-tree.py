#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.is_end = False
        self.children = {}

    def insert(self, word: str) -> None:
        if not word: 
            self.is_end = True
            return

        char = word[0]
        if char not in self.children:
            self.children[char] = Trie()
        self.children[char].insert(word[1:])
        
 
    def search(self, word: str) -> bool:
        if not word:
            return self.is_end

        char = word[0]
        if char not in self.children:
            return False

        return self.children[char].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True

        char = prefix[0]
        if char not in self.children:
            return False

        return self.children[char].startsWith(prefix[1:])

# @lc code=end

