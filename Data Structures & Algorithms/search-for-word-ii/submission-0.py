from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.word: str | None = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        res: List[str] = []
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r: int, c: int, parent: TrieNode) -> None:
            ch = board[r][c]
            curr = parent.children.get(ch)
            if curr is None:
                return

            if curr.word is not None:
                res.append(curr.word)
                curr.word = None  # Avoid adding duplicate words

            board[r][c] = "#"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, curr)
            board[r][c] = ch

            # Prune leaf nodes that are no longer needed
            if not curr.children and curr.word is None:
                del parent.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res