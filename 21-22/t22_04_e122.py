from collections import deque
import sys


def compute_distances_to_target(
    n: int, target: int, rev_adj: list[list[int]], limit: int
) -> list[int]:
    """Знаходить найкоротшу відстань від кожної вершини до цілі за допомогою BFS."""
    unreachable = limit + 1
    dist = [unreachable] * (n + 1)
    dist[target] = 0
    queue = deque([target])

    while queue:
        u = queue.popleft()
        next_dist = dist[u] + 1
        if next_dist > limit:
            continue
        for prev_v in rev_adj[u]:
            if dist[prev_v] == unreachable:
                dist[prev_v] = next_dist
                queue.append(prev_v)

    return dist


def count_simple_routes(
    n: int,
    a: int,
    b: int,
    d: int,
    adj: list[list[int]],
    adj_sets: list[set[int]],
    rev_adj: list[list[int]],
) -> int:
    """Підраховує кількість простих шляхів з a до b довжиною не більше d."""
    if a == b:
        return 1

    dist_to_b = compute_distances_to_target(n, b, rev_adj, d)
    if dist_to_b[a] > d:
        return 0

    visited = [False] * (n + 1)
    visited[a] = True

    def dfs(u: int, rem_days: int) -> int:
        # Якщо залишився 1 день, досягти b можна лише прямим переходом u -> b
        if rem_days == 1:
            return 1 if b in adj_sets[u] else 0

        total = 0
        next_rem = rem_days - 1
        for v in adj[u]:
            if v == b:
                # Досягли кінцевої бази; далі не йдемо, щоб уникнути повторного відвідування b
                total += 1
            elif not visited[v] and dist_to_b[v] <= next_rem:
                visited[v] = True
                total += dfs(v, next_rem)
                visited[v] = False
        return total

    return dfs(a, d)


def main() -> None:
    """Зчитує параметри маршруту та орієнтовані переходи між турбазами."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    k = int(next(it))
    a = int(next(it))
    b = int(next(it))
    d = int(next(it))

    adj_sets: list[set[int]] = [set() for _ in range(n + 1)]
    adj: list[list[int]] = [[] for _ in range(n + 1)]
    rev_adj: list[list[int]] = [[] for _ in range(n + 1)]

    for _ in range(k):
        u = int(next(it))
        v = int(next(it))
        # Уникаємо дублювання однакових орієнтованих переходів і петель
        if u != v and v not in adj_sets[u]:
            adj_sets[u].add(v)
            adj[u].append(v)
            rev_adj[v].append(u)

    result = count_simple_routes(n, a, b, d, adj, adj_sets, rev_adj)
    sys.stdout.write(f"{result}\n")


if __name__ == "__main__":
    main()
