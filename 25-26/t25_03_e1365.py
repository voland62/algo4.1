import sys


def dijkstra_matrix(n: int, s: int, f: int, matrix: list[list[int]]) -> int:
    """Знаходить найкоротшу відстань від вершини s до f алгоритмом Дейкстри за матрицею суміжності."""
    inf = 10**18
    dist = [inf] * n
    visited = [False] * n
    dist[s] = 0

    for _ in range(n):
        u = -1
        best_dist = inf
        # Обираємо невідвідану вершину з найменшою поточною відстанню
        for i in range(n):
            if not visited[i] and dist[i] < best_dist:
                best_dist = dist[i]
                u = i

        if u == -1 or u == f:
            break

        visited[u] = True
        row = matrix[u]
        for v in range(n):
            weight = row[v]
            if weight != -1 and not visited[v]:
                cand = best_dist + weight
                if cand < dist[v]:
                    dist[v] = cand

    return -1 if dist[f] == inf else dist[f]


def main() -> None:
    """Зчитує матрицю суміжності орієнтованого графа та виводить найкоротшу відстань між s і f."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    s = int(next(it)) - 1
    f = int(next(it)) - 1

    matrix = [[int(next(it)) for _ in range(n)] for _ in range(n)]
    sys.stdout.write(f"{dijkstra_matrix(n, s, f, matrix)}\n")


if __name__ == "__main__":
    main()
