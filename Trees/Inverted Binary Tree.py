from __future__ import annotations

from collections import deque
from typing import Protocol


class BinaryTreeNode(Protocol):
    left: BinaryTreeNode | None
    right: BinaryTreeNode | None


def invert_tree_iterative(root: BinaryTreeNode | None) -> BinaryTreeNode | None:
    if root is None:
        return None

    queue: deque[BinaryTreeNode] = deque([root])

    while queue:
        current: BinaryTreeNode = queue.popleft()
        current.left, current.right = current.right, current.left

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return root


# Complexity:

# Time: O(n), where n is the number of nodes in the binary tree. Each node is visited once.

# Space: O(n), in the worst case, the queue will hold all nodes at the last level of the tree.


# Invert a binary tree using recursive approach.
def invert_tree(root: BinaryTreeNode | None) -> BinaryTreeNode | None:
    if root is None:
        return None

    # Swap the left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


# Complexity:

# Time: O(n), where n is the number of nodes in the binary tree. Each node is visited once.

# Space: O(h), where h is the height of the tree. In the worst case (skewed tree), the recursion stack can go up to h, which can be n in the case of a skewed tree. In a balanced tree, h would be log(n).
