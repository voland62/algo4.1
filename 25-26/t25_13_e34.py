import heapq
import sys


def max_delivery_time(
    max_node: int,
    start: int,
    winners: list[int],
    adj: list[list[tuple[int, int]]],
) -> int:
    """Знаходить час доставки призу найвіддаленішому призеру алгоритмом Дейкстри або повертає -1."""
    inf = 10**18
    dist = [inf] * (max_node + 1)
    dist[start] = 0
    pq: list[tuple[int, int]] = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, weight in adj[u]:
            cand = d + weight
            if cand < dist[v]:
                dist[v] = cand
                heapq.heappush(pq, (cand, v))

    worst_time = 0
    for winner in winners:
        if dist[winner] == inf:
            return -1
        if dist[winner] > worst_time:
            worst_time = dist[winner]

    return worst_time


def main() -> None:
    """Зчитує дані про відділення пошти та визначає результат розсилки подарунків."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    winners = [int(next(it)) for _ in range(m)]
    raw_edges = [(int(next(it)), int(next(it)), int(next(it))) for _ in range(k)]
    start = int(next(it))

    max_node = max([n, start, *winners])
    for u, v, _ in raw_edges:
        if u > max_node:
            max_node = u
        if v > max_node:
            max_node = v

    adj: list[list[tuple[int, int]]] = [[] for _ in range(max_node + 1)]
    for u, v, w in raw_edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    result = max_delivery_time(max_node, start, winners, adj)
    if result == -1:
        sys.stdout.write("It is not fault of sponsor...\n")
    else:
        sys.stdout.write(f"The good sponsor!\n{result}\n")


if __name__ == "__main__":
    main()
