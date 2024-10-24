class Trie:

    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False
    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                new_node = Trie()
                curr.child[index] = new_node

            curr = curr.child[index]
        curr.wordEnd = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                return False

            curr = curr.child[index]

        if curr.wordEnd:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                return False

            curr = curr.child[index]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)