from collections import (
    deque,
)  # Import deque from collections for efficient queue operations


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
