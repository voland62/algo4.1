from collections import deque
import sys


def find_last_burning_vertex(
    n: int, adj: list[list[int]], sources: list[int]
) -> tuple[int, int]:
    """Знаходить час займання останньої вершини та її мінімальний номер через BFS."""
    burn_time = [-1] * (n + 1)
    queue: deque[int] = deque()

    # Усі початкові точки підпалу спалахують одночасно на 0-й секунді
    for start in sources:
        if burn_time[start] == -1:
            burn_time[start] = 0
            queue.append(start)

    while queue:
        u = queue.popleft()
        next_time = burn_time[u] + 1
        for v in adj[u]:
            if burn_time[v] == -1:
                burn_time[v] = next_time
                queue.append(v)

    max_time = -1
    best_vertex = 1
    # Перебираємо вершини за зростанням номера, тому при рівності збережеться найменший
    for v in range(1, n + 1):
        if burn_time[v] > max_time:
            max_time = burn_time[v]
            best_vertex = v

    return max_time, best_vertex


def main() -> None:
    """Зчитує граф павутини, точки підпалу та виводить результат моделювання."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    m = int(next(it))

    adj: list[list[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    k = int(next(it))
    sources = [int(next(it)) for _ in range(k)]

    max_time, best_vertex = find_last_burning_vertex(n, adj, sources)
    sys.stdout.write(f"{max_time}\n{best_vertex}\n")


if __name__ == "__main__":
    main()
