import sys


def max_shortest_distance(n: int, dist: list[list[int]], inf: int) -> int:
    """Знаходить максимальну скінченну найкоротшу відстань між парами вершин алгоритмом Флойда — Воршелла."""
    for k in range(n):
        row_k = dist[k]
        for i in range(n):
            row_i = dist[i]
            dik = row_i[k]
            if dik == inf:
                continue
            for j in range(n):
                dkj = row_k[j]
                if dkj == inf:
                    continue
                cand = dik + dkj
                if cand < row_i[j]:
                    row_i[j] = cand

    best = 0
    for i in range(n):
        row_i = dist[i]
        for j in range(n):
            val = row_i[j]
            if val != inf and val > best:
                best = val
    return best


def main() -> None:
    """Зчитує матрицю ваг графа (-1 означає відсутність ребра) та виводить максимальну найкоротшу відстань."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    inf = 10**18

    # Замінюємо -1 на нескінченність (відсутнє ребро)
    dist: list[list[int]] = []
    for _ in range(n):
        row: list[int] = []
        for _ in range(n):
            w = int(next(it))
            row.append(inf if w == -1 else w)
        dist.append(row)

    sys.stdout.write(f"{max_shortest_distance(n, dist, inf)}\n")


if __name__ == "__main__":
    main()
