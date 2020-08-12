from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    s = {}

    # loop over ancestors, add
    for parent, child in ancestors:
        if child not in s:
            s[child] = [parent]
        else:
            s[child].append(parent)

    # return -1 if starting node has no parents
    if starting_node not in s:
        return -1

    # else return depth first search
    return g.dfs(starting_node, s)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 6))