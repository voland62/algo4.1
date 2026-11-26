from collections import deque
import sys


def find_shortest_path(n: int, grid: list[list[str]]) -> list[list[str]] | None:
    """Знаходить найкоротший шлях від '@' до 'X' через BFS і позначає його '+'."""
    start_idx = -1
    target_idx = -1

    for r in range(n):
        row = grid[r]
        for c in range(n):
            cell = row[c]
            if cell == "@":
                start_idx = r * n + c
            elif cell == "X":
                target_idx = r * n + c

    if start_idx == -1 or target_idx == -1:
        return None

    total = n * n
    parent = [-1] * total
    parent[start_idx] = start_idx
    queue = deque([start_idx])

    while queue:
        idx = queue.popleft()
        if idx == target_idx:
            break

        r, c = divmod(idx, n)
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < n and 0 <= nc < n:
                nidx = nr * n + nc
                if parent[nidx] == -1 and grid[nr][nc] in (".", "X"):
                    parent[nidx] = idx
                    queue.append(nidx)

    if parent[target_idx] == -1:
        return None

    # Відновлюємо шлях від 'X' до '@', залишаючи початкову позначку '@' без змін
    curr = target_idx
    while curr != start_idx:
        r, c = divmod(curr, n)
        grid[r][c] = "+"
        curr = parent[curr]

    return grid


def main() -> None:
    """Зчитує таблицю лабіринту та виводить найкоротший шлях або 'N'."""
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    grid = [list(tokens[i + 1]) for i in range(n)]

    result = find_shortest_path(n, grid)
    if result is None:
        sys.stdout.write("N\n")
    else:
        lines = ["Y", *("".join(row) for row in result)]
        sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
