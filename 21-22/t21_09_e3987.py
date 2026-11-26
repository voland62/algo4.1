import sys


def is_complete_graph(n: int, m: int, tokens: list[bytes]) -> bool:
    """Перевіряє, чи з'єднана кожна пара різних вершин неорієнтованого графа."""
    unique_edges: set[tuple[int, int]] = set()
    it = iter(tokens[2:])

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        # Ігноруємо можливі петлі та нормалізуємо неорієнтовану пару вершин
        if u == v:
            continue
        pair = (u, v) if u < v else (v, u)
        unique_edges.add(pair)

    expected_edges = n * (n - 1) // 2
    return len(unique_edges) == expected_edges


def main() -> None:
    """Зчитує список ребер неорієнтованого графа та перевіряє його на повноту."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    m = int(tokens[1])
    sys.stdout.write("YES\n" if is_complete_graph(n, m, tokens) else "NO\n")


if __name__ == "__main__":
    main()
