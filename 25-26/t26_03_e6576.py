import heapq
import sys


def is_edge_in_mst(n: int, adj: list[list[tuple[int, int]]], p: int, q: int) -> bool:
    """Перевіряє за алгоритмом Прима, чи належить ребро (p, q) єдиному мінімальному кістяковому дереву."""
    if p == q:
        return False

    inf = 10**18
    visited = [False] * (n + 1)
    best = [inf] * (n + 1)
    parent = [0] * (n + 1)

    # Починаємо обхід Прима з вершини p: тоді (p, q) входить до МКД точно тоді, коли parent[q] == p
    best[p] = 0
    heap: list[tuple[int, int]] = [(0, p)]

    while heap:
        _, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        if u == q:
            break

        for v, w in adj[u]:
            if not visited[v] and w < best[v]:
                best[v] = w
                parent[v] = u
                heapq.heappush(heap, (w, v))

    return visited[q] and parent[q] == p


def main() -> None:
    """Зчитує тести та визначає для кожного, чи входить дорога (p, q) у мінімальне кістякове дерево."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    t = int(next(it))
    out: list[str] = []

    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        p = int(next(it))
        q = int(next(it))

        adj: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            w = int(next(it))
            adj[u].append((v, w))
            adj[v].append((u, w))

        out.append("YES" if is_edge_in_mst(n, adj, p, q) else "NO")

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
