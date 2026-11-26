import sys


def floyd_warshall(n: int, dist: list[list[int]]) -> None:
    """Обчислює матрицю найкоротших відстаней між усіма парами вершин алгоритмом Флойда — Воршелла."""
    for k in range(n):
        row_k = dist[k]
        for i in range(n):
            row_i = dist[i]
            dik = row_i[k]
            for j in range(n):
                cand = dik + row_k[j]
                if cand < row_i[j]:
                    row_i[j] = cand


def main() -> None:
    """Зчитує матрицю суміжності графа та виводить матрицю найкоротших відстаней."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    dist = [[int(next(it)) for _ in range(n)] for _ in range(n)]

    floyd_warshall(n, dist)

    out = "\n".join(" ".join(map(str, row)) for row in dist)
    sys.stdout.write(f"{out}\n")


if __name__ == "__main__":
    main()
