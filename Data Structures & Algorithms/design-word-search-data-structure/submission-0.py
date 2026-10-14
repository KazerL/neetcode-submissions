class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()

            node = node.children[char] 
        
        node.end = True

    def search(self, word: str) -> bool:
        # dfs recursive traversal
        def dfs(node, i):
            if i == len(word):
                return node.end

            char = word[i]

            if char == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            if char not in node.children:
                return False
            return dfs(node.children[char], i + 1)

        return dfs(self, 0)