def num_of_items_greater_than_k(root, k):
    cur = root
    while cur is not None and cur.item < k:
        cur = cur.right

    return count_nodes(k.right)

O(log n)