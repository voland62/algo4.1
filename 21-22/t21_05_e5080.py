import sys


def count_pendant_vertices(n: int, tokens: list[bytes]) -> int:
    """Обчислює кількість висячих вершин (степеня 1) за матрицею суміжності."""
    it = iter(tokens[1:])
    pendant_count = 0

    for _ in range(n):
        degree = 0
        for _ in range(n):
            # У простому незваженому графі суміжність позначається одиницею
            if next(it) != b"0":
                degree += 1
        if degree == 1:
            pendant_count += 1

    return pendant_count


def main() -> None:
    """Зчитує матрицю суміжності та виводить кількість висячих вершин графа."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    sys.stdout.write(f"{count_pendant_vertices(n, tokens)}\n")


if __name__ == "__main__":
    main()
