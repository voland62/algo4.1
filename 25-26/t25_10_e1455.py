import sys


def find_negative_cycle(n: int, edges: list[tuple[int, int, int]]) -> list[int]:
    """Знаходить будь-який цикл від'ємної ваги у графі алгоритмом Беллмана-Форда."""
    # Ініціалізація нулями еквівалентна фіктивній вершині з ребрами ваги 0 до всіх вершин
    dist = [0] * (n + 1)
    parent = [-1] * (n + 1)
    last_updated = -1

    for _ in range(n):
        last_updated = -1
        for u, v, w in edges:
            cand = dist[u] + w
            if cand < dist[v]:
                dist[v] = cand
                parent[v] = u
                last_updated = v
        if last_updated == -1:
            return []

    # Піднімаємося по батьківських вказівниках n разів, щоб гарантовано потрапити в сам цикл
    x = last_updated
    for _ in range(n):
        x = parent[x]

    # Відновлюємо вершини циклу в зворотному порядку, а потім розвертаємо
    cycle = [x]
    cur = parent[x]
    while cur != x:
        cycle.append(cur)
        cur = parent[cur]
    cycle.append(x)
    cycle.reverse()
    return cycle


def main() -> None:
    """Зчитує матрицю суміжності графа та виводить знайдений від'ємний цикл або NO."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    no_edge = 100000

    edges: list[tuple[int, int, int]] = []
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            w = int(next(it))
            if w != no_edge:
                edges.append((u, v, w))

    cycle = find_negative_cycle(n, edges)
    if not cycle:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write(f"YES\n{len(cycle)}\n{' '.join(map(str, cycle))}\n")


if __name__ == "__main__":
    main()
