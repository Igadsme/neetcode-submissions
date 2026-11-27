class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(idx: int, node: TrieNode) -> bool:
            if idx == len(word):
                return node.is_end

            ch = word[idx]
            if ch == ".":
                for child in node.children.values():
                    if dfs(idx + 1, child):
                        return True
                return False

            if ch not in node.children:
                return False
            return dfs(idx + 1, node.children[ch])

        return dfs(0, self.root)