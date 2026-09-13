# Find the maximum depth of a binary tree using Breadth-First Search (BFS).

from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def max_depth_bfs(root: "TreeNode") -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth


# Complexity:

# Time: O(n) — each node is visited once.

# Space: O(n) — in the worst case, the queue will hold all nodes at the deepest level of the tree.

# Find the maximum depth of a binary tree using Depth-First Search (DFS) recursively.


def max_depth(root: "TreeNode | None") -> int:
    # 1. Base Case: An empty tree has a depth of 0.
    if root is None:
        return 0

    # 2. Recursively find the depth of left and right subtrees.
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # 3. Take the larger depth and add 1 for the current node.
    return max(left_depth, right_depth) + 1


# Complexity:

# Time: O(n), where n is the number of nodes in the tree. Each node is visited once.

# Space: O(h), where h is the height of the tree. This space is used by the recursion stack. In the worst case (a completely unbalanced tree), the height of the tree can be n, leading to O(n) space complexity. In the best case (a balanced tree), the height is log(n), leading to O(log(n)) space complexity.
