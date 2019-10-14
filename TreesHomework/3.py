def nodes_at_level(root, d):
    if root is None:
        return 0

    if d == 0:
        return 1

    count_left = nodes_at_level(root.left, d - 1)
    count_right = nodes_at_level(root.right, d - 1)

    return count_left + count_right