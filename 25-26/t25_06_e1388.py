import heapq
import sys


def min_fuel_cost(n: int, costs: list[int], adj: list[list[int]]) -> int:
    """Обчислює мінімальну вартість подорожі з міста 1 до n алгоритмом Дейкстри."""
    inf = 10**18
    dist = [inf] * (n + 1)
    dist[1] = 0
    pq: list[tuple[int, int]] = [(0, 1)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == n:
            return d

        # Переїзд із міста u в сусіднє місто v вимагає купівлі одного повного бака в місті u
        next_cost = d + costs[u]
        for v in adj[u]:
            if next_cost < dist[v]:
                dist[v] = next_cost
                heapq.heappush(pq, (next_cost, v))

    return -1


def main() -> None:
    """Зчитує ціни на пальне та дороги (незалежно від розбиття на рядки) і знаходить оптимальний маршрут."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    costs = [0] + [int(next(it)) for _ in range(n)]
    m = int(next(it))

    adj: list[list[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    sys.stdout.write(f"{min_fuel_cost(n, costs, adj)}\n")


if __name__ == "__main__":
    main()
