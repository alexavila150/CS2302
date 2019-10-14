def get_max(root):
    cur = root
    while cur is not None:
        cur = cur.right

    return cur.item

O(log n)