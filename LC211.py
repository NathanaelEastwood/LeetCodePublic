class WordDictionary:

    def __init__(self):
        self.child = [None] * 26
        self.word_end = False
    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            c_index = ord(c) - ord('a')
            if curr.child[c_index] is None:
                curr.child[c_index] = WordDictionary()

            curr = curr.child[c_index]
        curr.word_end = True

    def search(self, word: str) -> bool:
        return self.dfs_search(word, self)

    def dfs_search(self, word: str, root):
        if len(word) == 0 and root.word_end:
            return True
        elif len(word) == 0:
            return False

        result = False
        if word[0] == '.':
            word = word[1:]
            for i in root.child:
                if i:
                    result = result or self.dfs_search(word, i)
        else:
            c_index = ord(word[0]) - ord('a')
            if root.child[c_index]:
                result = result or self.dfs_search(word[1:], root.child[c_index])
            else:
                return False

        return result


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)