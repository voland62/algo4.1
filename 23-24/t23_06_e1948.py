import sys


def topological_sort(
    n: int, adj: list[list[int]], in_degree: list[int]
) -> list[int] | None:
    """Виконує топологічне сортування алгоритмом Кана; повертає None за наявності циклу."""
    # Починаємо з усіх вершин, що не мають вхідних ребер; order водночас слугує чергою
    order = [v for v in range(1, n + 1) if in_degree[v] == 0]
    head = 0

    while head < len(order):
        u = order[head]
        head += 1
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                order.append(v)

    if len(order) != n:
        return None
    return order


def main() -> None:
    """Зчитує орієнтований граф і виводить топологічний порядок вершин або -1."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = map(int, tokens)
    n = next(it)
    m = next(it)

    adj: list[list[int]] = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        in_degree[v] += 1

    del tokens

    order = topological_sort(n, adj, in_degree)
    if order is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(map(str, order)) + "\n")


if __name__ == "__main__":
    main()
