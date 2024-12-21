from collections import defaultdict


def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def can_order_words(words):
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for word in words:
        start, end = word[0], word[-1]
        graph[start].add(end)
        out_degree[start] += 1
        in_degree[end] += 1

    start_node = end_node = None
    for node in set(in_degree.keys()) | set(out_degree.keys()):
        diff = out_degree[node] - in_degree[node]
        if diff > 1 or diff < -1:
            return False
        elif diff == 1:
            if start_node:
                return False
            start_node = node
        elif diff == -1:
            if end_node:
                return False
            end_node = node

    if not start_node:
        start_node = next(iter(graph))

    visited = set()
    dfs(graph, start_node, visited)

    return len(visited) == len(set(in_degree.keys()) | set(out_degree.keys()))


T = int(input())

for _ in range(T):
    N = int(input())

    words = [input().strip() for _ in range(N)]

    if can_order_words(words):
        print("Ordering is possible.")
    else:
        print("The door cannot be opened.")
