from collections.abc import Iterator
import sys


def iter_connected_components(
    n: int, adj: list[list[int]]
) -> Iterator[list[int]]:
    """Послідовно знаходить компоненти зв'язності неорієнтованого графа методом BFS."""
    visited = bytearray(n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue

        visited[start] = 1
        # Список component використовується одночасно як черга BFS і як результат
        component = [start]
        head = 0
        while head < len(component):
            u = component[head]
            head += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = 1
                    component.append(v)

        yield component


def iter_ints() -> Iterator[int]:
    """Потоково зчитує цілі числа зі стандартного введення без збереження всього тексту."""
    for line in sys.stdin.buffer:
        for token in line.split():
            yield int(token)


def main() -> None:
    """Зчитує неорієнтований граф, знаходить компоненти зв'язності та виводить їх."""
    it = iter_ints()
    n = next(it, None)
    if n is None:
        return
    m = next(it)

    adj: list[list[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        # Петлі не впливають на зв'язність вершин, тому пропускаємо їх
        if u != v:
            adj[u].append(v)
            adj[v].append(u)

    blocks: list[str] = []
    for component in iter_connected_components(n, adj):
        blocks.append(f"{len(component)}\n{' '.join(map(str, component))}")

    del adj

    sys.stdout.write(f"{len(blocks)}\n" + "\n".join(blocks) + "\n")


if __name__ == "__main__":
    main()
