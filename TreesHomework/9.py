def num_keys(root):
    if root.is_leaf:
        return len(root.keys)

    num_keys_subtrees = 0
    for child in root.children:
        num_keys_subtrees += num_keys(child)

    return num_keys_subtrees
