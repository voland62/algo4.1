import math
import sys


def prim_euclidean_mst(xs: list[int], ys: list[int]) -> float:
    """Обчислює довжину евклідового МКД алгоритмом Прима без побудови списку ребер."""
    n = len(xs)
    if n <= 1:
        return 0.0

    inf = 10**18
    # Розбиваємо точки на 2D-блоки, щоб відсікати явно далекі блоки за обмежувальним прямокутником
    pts = sorted(zip(xs, ys))
    block_size = 64
    strip_size = max(1, int(math.sqrt(n * block_size)))
    blocks: list[list] = []
    for i in range(0, n, strip_size):
        strip = sorted(pts[i : i + strip_size], key=lambda p: p[1])
        for j in range(0, len(strip), block_size):
            chunk = strip[j : j + block_size]
            bx = [p[0] for p in chunk]
            by = [p[1] for p in chunk]
            bd = [inf] * len(chunk)
            blocks.append([min(bx), max(bx), by[0], by[-1], bx, by, bd, inf, inf, inf, 0])

    b0 = blocks[0]
    ux = b0[4].pop(0)
    uy = b0[5].pop(0)
    b0[6].pop(0)
    if not b0[4]:
        blocks.pop(0)
    else:
        b0[0] = min(b0[4])
        b0[1] = max(b0[4])
        b0[2] = min(b0[5])
        b0[3] = max(b0[5])

    visited_pts = [(ux, uy)]
    for blk in blocks:
        min_x, max_x, min_y, max_y = blk[0], blk[1], blk[2], blk[3]
        dx = min_x - ux if ux < min_x else (ux - max_x if ux > max_x else 0)
        dy = min_y - uy if uy < min_y else (uy - max_y if uy > max_y else 0)
        blk[9] = dx * dx + dy * dy

    total = 0.0
    sqrt = math.sqrt

    for _ in range(n - 1):
        while True:
            best_bi = 0
            best_lb = blocks[0][9]
            for bi in range(1, len(blocks)):
                lb = blocks[bi][9]
                if lb < best_lb:
                    best_lb = lb
                    best_bi = bi

            blk = blocks[best_bi]
            flushed = blk[10]
            total_vis = len(visited_pts)
            if flushed == total_vis:
                break

            # Відкладено оновлюємо блок від нових відвіданих точок, починаючи з найближчих до прямокутника
            min_x, max_x, min_y, max_y, bx, by, bd, max_bd, min_bd, _, _ = blk
            cands: list[tuple[int, int, int]] = []
            for k in range(flushed, total_vis):
                px, py = visited_pts[k]
                dx = min_x - px if px < min_x else (px - max_x if px > max_x else 0)
                dy = min_y - py if py < min_y else (py - max_y if py > max_y else 0)
                d_box = dx * dx + dy * dy
                if d_box < max_bd:
                    cands.append((d_box, px, py))
            if len(cands) > 1:
                cands.sort()

            m = len(bd)
            for d_box, px, py in cands:
                if d_box >= max_bd:
                    break
                new_max = 0
                new_min = inf
                for vi in range(m):
                    dx = px - bx[vi]
                    dy = py - by[vi]
                    nd = dx * dx + dy * dy
                    cur = bd[vi]
                    if nd < cur:
                        bd[vi] = nd
                        cur = nd
                    if cur > new_max:
                        new_max = cur
                    if cur < new_min:
                        new_min = cur
                max_bd = new_max
                min_bd = new_min

            blk[7] = max_bd
            blk[8] = min_bd
            blk[9] = min_bd
            blk[10] = total_vis

        best_d = blk[8]
        bx, by, bd = blk[4], blk[5], blk[6]
        best_vi = bd.index(best_d)
        total += sqrt(best_d)
        ux = bx[best_vi]
        uy = by[best_vi]

        last = len(bd) - 1
        if best_vi != last:
            bx[best_vi] = bx[last]
            by[best_vi] = by[last]
            bd[best_vi] = bd[last]
        bx.pop()
        by.pop()
        bd.pop()
        if not bd:
            blocks.pop(best_bi)
        else:
            blk[7] = max(bd)
            blk[8] = min(bd)
            blk[9] = blk[8]

        visited_pts.append((ux, uy))
        for b in blocks:
            min_x, max_x, min_y, max_y = b[0], b[1], b[2], b[3]
            dx = min_x - ux if ux < min_x else (ux - max_x if ux > max_x else 0)
            dy = min_y - uy if uy < min_y else (uy - max_y if uy > max_y else 0)
            d_box = dx * dx + dy * dy
            if d_box < b[9]:
                b[9] = d_box

    return total


def main() -> None:
    """Зчитує координати міст і виводить мінімальну сумарну довжину доріг для їх з'єднання."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    xs = [0] * n
    ys = [0] * n
    for i in range(n):
        xs[i] = int(next(it))
        ys[i] = int(next(it))

    ans = prim_euclidean_mst(xs, ys)
    sys.stdout.write(f"{ans:.10f}\n")


if __name__ == "__main__":
    main()
