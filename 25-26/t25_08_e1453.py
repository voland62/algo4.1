import sys


def bellman_ford(n: int, edges: list[tuple[int, int, int]]) -> list[int]:
    """Обчислює найкоротші відстані від вершини 1 до всіх вершин алгоритмом Беллмана-Форда."""
    inf = 10**9
    unreachable_value = 30000
    dist = [inf] * (n + 1)
    dist[1] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            du = dist[u]
            if du != inf and du + w < dist[v]:
                dist[v] = du + w
                changed = True
        if not changed:
            break

    return [unreachable_value if dist[i] == inf else dist[i] for i in range(1, n + 1)]


def main() -> None:
    """Зчитує зважений орієнтований граф і виводить найкоротші відстані від першої вершини."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    m = int(next(it))

    edges: list[tuple[int, int, int]] = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))

    result = bellman_ford(n, edges)
    sys.stdout.write(f"{' '.join(map(str, result))}\n")


if __name__ == "__main__":
    main()
