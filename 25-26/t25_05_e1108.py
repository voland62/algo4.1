import sys


def has_negative_cycle(n: int, edges: list[tuple[int, int, int]]) -> bool:
    """Перевіряє наявність циклу від'ємної ваги, досяжного з вершини 0, алгоритмом Беллмана-Форда."""
    inf = 10**18
    dist = [inf] * n
    dist[0] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            du = dist[u]
            if du != inf and du + w < dist[v]:
                dist[v] = du + w
                changed = True
        if not changed:
            return False

    # На n-й ітерації релаксація можлива лише за наявності циклу від'ємної ваги
    for u, v, w in edges:
        du = dist[u]
        if du != inf and du + w < dist[v]:
            return True

    return False


def main() -> None:
    """Зчитує систему червоточин і визначає можливість нескінченно повертатися в минуле."""
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

    result = "possible" if has_negative_cycle(n, edges) else "not possible"
    sys.stdout.write(f"{result}\n")


if __name__ == "__main__":
    main()
