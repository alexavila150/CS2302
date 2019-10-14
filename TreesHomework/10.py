def get_smallest_key_at_d(root, d):
    cur = root
    while cur is not None:
        if d == 0:
            return cur.key[0]
        d -= 1
        cur = cur.left

    return 1