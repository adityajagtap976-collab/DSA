def max_depth(root):
    # 1. Base Case: An empty tree has a depth of 0.
    if root is None:
        return 0

    # 2. Recursively find the depth of left and right subtrees.
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # 3. Take the larger depth and add 1 for the current node.
    return max(left_depth, right_depth) + 1


# Time complexity: O(n), where n is the number of nodes in the tree. Each node is visited once.
# Space complexity: O(h), where h is the height of the tree. This space is used by the recursion stack. In the worst case (a completely unbalanced tree), the height of the tree can be n, leading to O(n) space complexity. In the best case (a balanced tree), the height is log(n), leading to O(log(n)) space complexity.
