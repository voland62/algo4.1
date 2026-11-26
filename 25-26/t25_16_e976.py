import sys


def shortest_path_existence(n: int, dist: list[list[int]], inf: int) -> list[list[int]]:
    """Визначає для кожної пари вершин існування найкоротшого шляху (0, 1 або 2) за Флойдом — Воршеллом."""
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
                if cand < -inf:
                    # Обмежуємо знизу, щоб уникнути експоненційного зростання на від'ємних циклах
                    cand = -inf
                if cand < row_i[j]:
                    row_i[j] = cand

    status = [[0 if dist[i][j] == inf else 1 for j in range(n)] for i in range(n)]

    # Вершина k з dist[k][k] < 0 лежить на циклі від'ємної ваги (включно з від'ємними петлями)
    for k in range(n):
        if dist[k][k] < 0:
            row_k = dist[k]
            for i in range(n):
                if dist[i][k] < inf:
                    status_i = status[i]
                    for j in range(n):
                        if row_k[j] < inf:
                            status_i[j] = 2

    return status


def main() -> None:
    """Зчитує матрицю суміжності та виводить матрицю існування найкоротших шляхів."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    inf = 10**9

    dist: list[list[int]] = []
    for i in range(n):
        row: list[int] = []
        for j in range(n):
            w = int(next(it))
            if i == j:
                # Від'ємну петлю зберігаємо, інакше найкоротша тривіальна відстань до себе дорівнює 0
                row.append(w if w < 0 else 0)
            else:
                row.append(inf if w == 0 else w)
        dist.append(row)

    status = shortest_path_existence(n, dist, inf)
    out = "\n".join(" ".join(map(str, row)) for row in status)
    sys.stdout.write(f"{out}\n")


if __name__ == "__main__":
    main()
