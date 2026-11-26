import sys


def average_shortest_distance(n: int, dist: list[list[int]], inf: int) -> float:
    """Знаходить середню довжину найкоротшого шляху між усіма досяжними парами різних міст за Флойдом — Воршеллом."""
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

    total_length = 0
    pair_count = 0
    for i in range(n):
        row_i = dist[i]
        for j in range(n):
            if i != j and row_i[j] < inf:
                total_length += row_i[j]
                pair_count += 1

    return 0.0 if pair_count == 0 else total_length / pair_count


def main() -> None:
    """Зчитує орієнтовану дорожню мережу та виводить середню відстань з 6 знаками після крапки."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    k = int(next(it))
    inf = 10**18

    dist = [[inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for _ in range(k):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        length = int(next(it))
        if length < dist[a][b]:
            dist[a][b] = length

    ans = average_shortest_distance(n, dist, inf)
    sys.stdout.write(f"{ans:.6f}\n")


if __name__ == "__main__":
    main()
