import heapq
import sys


def dijkstra_with_path(
    n: int, s: int, f: int, adj: list[list[tuple[int, int]]]
) -> tuple[int, list[int]]:
    """Знаходить найкоротший шлях між вершинами s та f за допомогою алгоритму Дейкстри."""
    inf = 10**18
    dist = [inf] * (n + 1)
    parent = [-1] * (n + 1)
    dist[s] = 0
    pq: list[tuple[int, int]] = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == f:
            break

        for v, weight in adj[u]:
            cand = d + weight
            if cand < dist[v]:
                dist[v] = cand
                parent[v] = u
                heapq.heappush(pq, (cand, v))

    if dist[f] == inf:
        return -1, []

    # Відновлюємо маршрут від кінцевої вершини до початкової
    path: list[int] = []
    cur = f
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return dist[f], path


def main() -> None:
    """Зчитує неорієнтований граф і виводить довжину та вершини найкоротшого шляху."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    m = int(next(it))
    s = int(next(it))
    f = int(next(it))

    adj: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    length, path = dijkstra_with_path(n, s, f, adj)
    if length == -1:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(f"{length}\n{' '.join(map(str, path))}\n")


if __name__ == "__main__":
    main()
