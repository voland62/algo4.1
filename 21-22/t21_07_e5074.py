import sys


def compute_vertex_degrees(n: int, m: int, tokens: list[bytes]) -> list[int]:
    """Обчислює степені всіх вершин неорієнтованого графа за списком ребер."""
    degrees = [0] * (n + 1)

    it = iter(tokens[2:])
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        degrees[u] += 1
        degrees[v] += 1

    return degrees


def main() -> None:
    """Зчитує список ребер неорієнтованого графа та виводить степені всіх вершин."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    m = int(tokens[1])
    degrees = compute_vertex_degrees(n, m, tokens)

    lines = [str(degrees[v]) for v in range(1, n + 1)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
