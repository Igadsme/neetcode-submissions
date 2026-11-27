from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        cloned: dict[Node, Node] = {}

        def dfs(curr: Node) -> Node:
            if curr in cloned:
                return cloned[curr]

            copy = Node(curr.val)
            cloned[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)