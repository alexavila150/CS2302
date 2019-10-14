def get_max_at_depth(root, d):
    cur = root
    while cur is not None
        if d == 0:
            return cur
        d -= 1
        cur = cur.right

    return None

O(log N)