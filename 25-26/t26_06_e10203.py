import math
import sys


def min_radio_range(s: int, p: int, xs: list[int], ys: list[int]) -> float:
    """Знаходить s-те найбільше ребро МКД алгоритмом Прима (мінімальну дальність радіозв'язку)."""
    if s >= p:
        return 0.0

    # Зберігаємо невідвідані вершини у компактних списках для щільного Прима за O(p^2)
    ax = xs[1:]
    ay = ys[1:]
    ux = xs[0]
    uy = ys[0]
    ad = [(ux - ax[i]) * (ux - ax[i]) + (uy - ay[i]) * (uy - ay[i]) for i in range(p - 1)]

    mst_sq: list[int] = []
    while ad:
        best_d = min(ad)
        idx = ad.index(best_d)
        mst_sq.append(best_d)

        ux = ax[idx]
        uy = ay[idx]
        last = len(ad) - 1
        if idx != last:
            ax[idx] = ax[last]
            ay[idx] = ay[last]
            ad[idx] = ad[last]
        ax.pop()
        ay.pop()
        ad.pop()

        for i in range(last):
            dx = ux - ax[i]
            dy = uy - ay[i]
            nd = dx * dx + dy * dy
            if nd < ad[i]:
                ad[i] = nd

    # Супутники прибирають (s - 1) найдовших ребер МКД; залишається ребро з індексом (p - 1) - s
    mst_sq.sort()
    return math.sqrt(mst_sq[p - 1 - s])


def main() -> None:
    """Зчитує тести та виводить мінімальне d з точністю до двох десяткових знаків."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    it = iter(tokens)
    t = int(next(it))
    out: list[str] = []

    for _ in range(t):
        s = int(next(it))
        p = int(next(it))
        xs = [0] * p
        ys = [0] * p
        for i in range(p):
            xs[i] = int(next(it))
            ys[i] = int(next(it))
        out.append(f"{min_radio_range(s, p, xs, ys):.2f}")

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
