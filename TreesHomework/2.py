def depth(root, node):
    depth = 0
    cur = root
    while cur is not None:
        if cur.item == node.item:
            return depth
        elif cur.item < node.item:
            cur = cur.left
        elif cur.item > node.item:
            cur = cur.right
        depth += 1

    return None # if Node not found