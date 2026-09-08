def invert_tree(root):
    if root is None:
        return None

    # Swap the left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root

# Time Complexity: O(n), where n is the number of nodes in the binary tree. Each node is visited once.