import sys


def count_paper_parts(m: int, n: int, grid: list[bytearray]) -> int:
    """Підраховує кількість 4-зв'язних компонент із клітинок '#'."""
    parts = 0
    sharp = ord("#")
    dot = ord(".")

    for r in range(m):
        row = grid[r]
        for c in range(n):
            if row[c] != sharp:
                continue

            parts += 1
            row[c] = dot
            # Ітеративний DFS уникає переповнення стека викликів на великих сітках
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                if cr > 0 and grid[cr - 1][cc] == sharp:
                    grid[cr - 1][cc] = dot
                    stack.append((cr - 1, cc))
                if cr + 1 < m and grid[cr + 1][cc] == sharp:
                    grid[cr + 1][cc] = dot
                    stack.append((cr + 1, cc))
                if cc > 0 and grid[cr][cc - 1] == sharp:
                    grid[cr][cc - 1] = dot
                    stack.append((cr, cc - 1))
                if cc + 1 < n and grid[cr][cc + 1] == sharp:
                    grid[cr][cc + 1] = dot
                    stack.append((cr, cc + 1))

    return parts


def main() -> None:
    """Зчитує аркуш паперу та виводить кількість його окремих частин."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    m = int(tokens[0])
    n = int(tokens[1])
    grid = [bytearray(tokens[i + 2]) for i in range(m)]

    sys.stdout.write(f"{count_paper_parts(m, n, grid)}\n")


if __name__ == "__main__":
    main()
