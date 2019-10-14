def search_for_k(root, k):
    if root is None:
        return -1

    if root.keys.contains(k):
        if root.is_leaf:
            return 0
        return 1

    i = 0
    for key in root.keys:
        if k < key:
            return search_for_k(root.children[i])
        i += 0

