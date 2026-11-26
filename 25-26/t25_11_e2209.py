import heapq
import sys


def min_elevator_cost(
    target_floor: int,
    up_cost: int,
    down_cost: int,
    enter_cost: int,
    exit_cost: int,
    elevators: list[list[int]],
) -> int:
    """Знаходить мінімальну вартість підйому на поверх target_floor алгоритмом Дейкстри зі стисненням координат."""
    floor_set = {1, target_floor}
    for stops in elevators:
        floor_set.update(stops)

    floors = sorted(floor_set)
    num_floors = len(floors)
    floor_to_idx = {floor: idx for idx, floor in enumerate(floors)}

    # Вершини 0..num_floors-1 відповідають стисненим поверхам, далі йдуть вузли-хаби ліфтів
    total_nodes = num_floors + len(elevators)
    adj: list[list[tuple[int, int]]] = [[] for _ in range(total_nodes)]

    for i in range(num_floors - 1):
        diff = floors[i + 1] - floors[i]
        adj[i].append((i + 1, diff * up_cost))
        adj[i + 1].append((i, diff * down_cost))

    for elev_idx, stops in enumerate(elevators):
        hub = num_floors + elev_idx
        for floor in stops:
            node = floor_to_idx[floor]
            adj[node].append((hub, enter_cost))
            adj[hub].append((node, exit_cost))

    start_node = floor_to_idx[1]
    target_node = floor_to_idx[target_floor]

    inf = 10**18
    dist = [inf] * total_nodes
    dist[start_node] = 0
    pq: list[tuple[int, int]] = [(0, start_node)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == target_node:
            return d

        for v, weight in adj[u]:
            cand = d + weight
            if cand < dist[v]:
                dist[v] = cand
                heapq.heappush(pq, (cand, v))

    return dist[target_node]


def main() -> None:
    """Зчитує параметри будинку й ліфтів та виводить мінімальну вартість підйому сейфа."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    target_floor = int(next(it))
    up_cost = int(next(it))
    down_cost = int(next(it))
    enter_cost = int(next(it))
    exit_cost = int(next(it))
    num_elevators = int(next(it))

    elevators: list[list[int]] = []
    for _ in range(num_elevators):
        k = int(next(it))
        elevators.append([int(next(it)) for _ in range(k)])

    ans = min_elevator_cost(
        target_floor, up_cost, down_cost, enter_cost, exit_cost, elevators
    )
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()
