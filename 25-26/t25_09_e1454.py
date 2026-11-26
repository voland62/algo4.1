from collections import deque
import sys


def bfs_reach(start: int, n: int, adj: list[list[int]]) -> list[bool]:
    """Знаходить усі вершини, досяжні з вершини start у графі."""
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return visited


def solve_knowledge_labyrinth(
    n: int, edges: list[tuple[int, int, int]]
) -> str:
    """Шукає максимальну кількість знань або виявляє додатний цикл алгоритмом Беллмана-Форда з чергою."""
    fwd_unweighted: list[list[int]] = [[] for _ in range(n + 1)]
    rev_unweighted: list[list[int]] = [[] for _ in range(n + 1)]
    for u, v, _ in edges:
        fwd_unweighted[u].append(v)
        rev_unweighted[v].append(u)

    # Залишаємо лише кімнати, досяжні зі старту 1 і з яких можна вийти у n
    reach_from_start = bfs_reach(1, n, fwd_unweighted)
    if not reach_from_start[n]:
        return ":("

    reach_to_exit = bfs_reach(n, n, rev_unweighted)
    active = [reach_from_start[i] and reach_to_exit[i] for i in range(n + 1)]
    active_count = sum(active)

    adj: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        if active[u] and active[v]:
            adj[u].append((v, w))

    ninf = -(10**18)
    dist = [ninf] * (n + 1)
    length = [0] * (n + 1)
    in_queue = [False] * (n + 1)

    dist[1] = 0
    queue = deque([1])
    in_queue[1] = True

    while queue:
        u = queue.popleft()
        in_queue[u] = False
        du = dist[u]
        lu = length[u] + 1

        for v, w in adj[u]:
            cand = du + w
            if cand > dist[v]:
                dist[v] = cand
                length[v] = lu
                # Шлях завдовжки щонайменше active_count ребер серед active_count вершин містить додатний цикл
                if lu >= active_count:
                    return ":)"
                if not in_queue[v]:
                    # Евристика першочергової обробки більших значень пришвидшує релаксацію максимумів
                    if queue and cand > dist[queue[0]]:
                        queue.appendleft(v)
                    else:
                        queue.append(v)
                    in_queue[v] = True

    return str(dist[n])


def main() -> None:
    """Зчитує опис лабіринту знань та виводить найкращий можливий результат."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)), int(next(it)), int(next(it))) for _ in range(m)]

    sys.stdout.write(f"{solve_knowledge_labyrinth(n, edges)}\n")


if __name__ == "__main__":
    main()
