import sys


def plan_new_highways(n: int, xs: list[int], ys: list[int], adj: list[list[int]]) -> list[str]:
    """Знаходить нові автомагістралі алгоритмом Прима за O(n^2), враховуючи існуючі дороги з вагою 0."""
    if n <= 1:
        return []

    inf = 10**18
    visited = [False] * n
    # Значення -1 позначає безкоштовну вже існуючу автомагістраль (менше за будь-яку квадратичну відстань)
    min_dist = [inf] * n
    parent = [-1] * n
    min_dist[0] = 0

    new_highways: list[str] = []

    for _ in range(n):
        u = -1
        best = inf + 1
        for i in range(n):
            if not visited[i] and min_dist[i] < best:
                best = min_dist[i]
                u = i

        visited[u] = True
        if parent[u] != -1 and min_dist[u] != -1:
            new_highways.append(f"{parent[u] + 1} {u + 1}")

        # Спочатку поширюємо 0-вагові ребра існуючих доріг
        for v in adj[u]:
            if not visited[v] and min_dist[v] != -1:
                min_dist[v] = -1
                parent[v] = u

        ux = xs[u]
        uy = ys[u]
        for v in range(n):
            if not visited[v] and min_dist[v] > 0:
                dx = ux - xs[v]
                dy = uy - ys[v]
                d = dx * dx + dy * dy
                if d < min_dist[v]:
                    min_dist[v] = d
                    parent[v] = u

    return new_highways


def main() -> None:
    """Зчитує тести та виводить перелік нових автомагістралей або 'No new highways need'."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    t = int(next(it))
    blocks_out: list[str] = []

    for _ in range(t):
        n = int(next(it))
        xs = [0] * n
        ys = [0] * n
        for i in range(n):
            xs[i] = int(next(it))
            ys[i] = int(next(it))

        m = int(next(it))
        adj: list[list[int]] = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(it)) - 1
            v = int(next(it)) - 1
            adj[u].append(v)
            adj[v].append(u)

        highways = plan_new_highways(n, xs, ys, adj)
        if highways:
            blocks_out.append("\n".join(highways))
        else:
            blocks_out.append("No new highways need")

    sys.stdout.write("\n\n".join(blocks_out) + "\n")


if __name__ == "__main__":
    main()
