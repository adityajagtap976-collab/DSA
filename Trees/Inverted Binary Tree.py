# Invert a binary tree using iterative approach.

from collections import (
    deque,
)
from logging import root  # Import deque from collections for efficient queue operations


def invert_tree_iterative(root):
    if not root:
        return None

    # Initialize queue with the root node
    queue = deque([root])

    while queue:
        current = queue.popleft()

        # Swap the left and right children
        current.left, current.right = current.right, current.left

        # Add the children to the queue for further processing
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return root


# 4. Call the function
inverted_root = invert_tree_iterative(root)


# Complexity:

# Time: O(n), where n is the number of nodes in the binary tree. Each node is visited once.

# Space: O(n), in the worst case, the queue will hold all nodes at the last level of the tree.


# Invert a binary tree using recursive approach.
def invert_tree(root):
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
