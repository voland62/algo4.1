import heapq
import sys


def earliest_arrival(
    n: int, start: int, target: int, adj: list[list[tuple[int, int, int]]]
) -> int:
    """Знаходить мінімальний час прибуття із села start до target за розкладом алгоритмом Дейкстри."""
    inf = 10**18
    best_time = [inf] * (n + 1)
    best_time[start] = 0
    pq: list[tuple[int, int]] = [(0, start)]

    while pq:
        cur_time, u = heapq.heappop(pq)
        if cur_time > best_time[u]:
            continue
        if u == target:
            return cur_time

        for dep, dest, arr in adj[u]:
            # Можна сісти лише на рейс, що відправляється не раніше моменту прибуття в село u
            if cur_time <= dep and arr < best_time[dest]:
                best_time[dest] = arr
                heapq.heappush(pq, (arr, dest))

    return -1


def main() -> None:
    """Зчитує розклад автобусів і виводить найменший можливий час досягнення пункту призначення."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    start = int(next(it))
    target = int(next(it))
    r = int(next(it))

    adj: list[list[tuple[int, int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(r):
        u = int(next(it))
        dep = int(next(it))
        v = int(next(it))
        arr = int(next(it))
        adj[u].append((dep, v, arr))

    sys.stdout.write(f"{earliest_arrival(n, start, target, adj)}\n")


if __name__ == "__main__":
    main()
