def sum_at_level(root, d):
    if root is None:
        return 0

    if d == 0:
        return root.item

    sum_left = sum_at_level(root.left, d - 1)
    sum_right = sum_at_level(root.right, d - 1)

    return sum_left + sum_right