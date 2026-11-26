import sys


def has_multiple_edges(m: int, tokens: list[bytes]) -> bool:
    """Перевіряє, чи містить орієнтований граф повторювані напрямлені ребра."""
    seen: set[tuple[int, int]] = set()
    it = iter(tokens[2:])

    for _ in range(m):
        # В орієнтованому графі пари (u, v) та (v, u) є різними ребрами
        edge = (int(next(it)), int(next(it)))
        if edge in seen:
            return True
        seen.add(edge)

    return False


def main() -> None:
    """Зчитує орієнтований граф та визначає наявність у ньому мультиребер."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    m = int(tokens[1])
    sys.stdout.write("YES\n" if has_multiple_edges(m, tokens) else "NO\n")


if __name__ == "__main__":
    main()
