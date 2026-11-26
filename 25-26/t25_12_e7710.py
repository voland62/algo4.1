import heapq
import sys

# Вершини та ваги до 10^4 уміщуються в 15 бітів, що дозволяє пакувати ребро в одне ціле число
_MASK = (1 << 15) - 1


def read_graph_stream() -> tuple[int, list[list[int]]]:
    """Потоково зчитує великий граф блоками для економії пам'яті та пакує суміжні ребра."""
    buf = sys.stdin.buffer
    tail = b""
    rem: list[int] = []
    header_needed = True
    n = 0
    skip_k = 0
    adj: list[list[int]] = []
    append_fn = []

    eof = False
    while not eof:
        chunk = buf.read(1 << 19)
        if not chunk:
            eof = True
            if not tail:
                break
            nums = list(map(int, tail.split()))
            tail = b""
        else:
            data = tail + chunk
            # Розрізаємо блок лише по пробільному символу, щоб не пошкодити жодне число
            idx = len(data) - 1
            while idx >= 0 and data[idx] > 32:
                idx -= 1
            if idx < 0:
                tail = data
                continue
            tail = data[idx + 1 :]
            nums = list(map(int, data[: idx + 1].split()))

        if rem:
            nums = rem + nums
            rem = []

        pos = 0
        if header_needed:
            if len(nums) < 3:
                rem = nums
                continue
            n = nums[0]
            skip_k = nums[2]
            adj = [[] for _ in range(n + 1)]
            append_fn = [lst.append for lst in adj]
            pos = 3
            header_needed = False

        if skip_k > 0:
            avail = len(nums) - pos
            if avail <= skip_k:
                skip_k -= avail
                continue
            pos += skip_k
            skip_k = 0

        usable = ((len(nums) - pos) // 3) * 3
        end = pos + usable
        for a, b, c in zip(
            nums[pos:end:3], nums[pos + 1 : end : 3], nums[pos + 2 : end : 3]
        ):
            shifted = c << 15
            append_fn[a](shifted | b)
            append_fn[b](shifted | a)

        if end < len(nums):
            rem = nums[end:]

    return n, adj


def has_alternative_shortest_path(n: int, adj: list[list[int]]) -> bool:
    """Перевіряє наявність принаймні двох найкоротших шляхів з 1 до n алгоритмом Дейкстри."""
    if n == 0:
        return False

    inf = 10**18
    dist = [inf] * (n + 1)
    ways = [0] * (n + 1)
    dist[1] = 0
    ways[1] = 1

    pq: list[tuple[int, int]] = [(0, 1)]
    heappop = heapq.heappop
    heappush = heapq.heappush
    mask = _MASK

    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        if u == n:
            break

        wu = ways[u]
        for edge in adj[u]:
            v = edge & mask
            cand = d + (edge >> 15)
            dv = dist[v]
            if cand < dv:
                dist[v] = cand
                ways[v] = wu
                heappush(pq, (cand, v))
            elif cand == dv and ways[v] < 2:
                # Достатньо розрізняти 0, 1 або >= 2 найкоротших шляхів
                total = ways[v] + wu
                ways[v] = 2 if total >= 2 else total

    return ways[n] >= 2


def main() -> None:
    """Зчитує дорожню мережу міста та визначає, чи існує інший найкоротший маршрут."""
    n, adj = read_graph_stream()
    if n == 0:
        return
    ans = "yes" if has_alternative_shortest_path(n, adj) else "no"
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()
