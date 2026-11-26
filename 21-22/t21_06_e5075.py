import sys


def compute_degrees(
    n: int, m: int, tokens: list[bytes]
) -> tuple[list[int], list[int]]:
    """Обчислює напівстепені входу та виходу кожної вершини орієнтованого графа."""
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    it = iter(tokens[2:])
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        out_degree[u] += 1
        in_degree[v] += 1

    return in_degree, out_degree


def main() -> None:
    """Зчитує список ребер орієнтованого графа та виводить півстепені кожної вершини."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    m = int(tokens[1])
    in_degree, out_degree = compute_degrees(n, m, tokens)

    # Для кожної вершини виводимо спочатку напівстепінь входу, потім — виходу
    lines = [f"{in_degree[v]} {out_degree[v]}" for v in range(1, n + 1)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
