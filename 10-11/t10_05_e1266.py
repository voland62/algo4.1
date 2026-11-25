import sys


def solve_cd(capacity: int, tracks: list[int]) -> int:
    """Знаходить максимальну суму тривалостей треків <= capacity повним перебором з відсіканням."""
    # Сортуємо треки за спаданням, щоб швидше знайти оптимальну суму та активніше відсікати гілки
    tracks_sorted = sorted(tracks, reverse=True)
    n = len(tracks_sorted)

    # Обчислюємо суфіксні суми для оцінки максимально можливої суми з індексу i
    suffix_sum = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + tracks_sorted[i]

    best = 0

    def backtrack(idx: int, current_sum: int) -> None:
        nonlocal best

        if current_sum > best:
            best = current_sum

        # Якщо вже досягли повної ємності касети або розглянули всі треки — зупиняємося
        if best == capacity or idx == n:
            return

        # Відсікання: навіть якщо взяти всі решту треків, краще за best не стане
        if current_sum + suffix_sum[idx] <= best:
            return

        # Гілка 1: пробуємо взяти поточний трек, якщо він поміщається
        track = tracks_sorted[idx]
        if current_sum + track <= capacity:
            backtrack(idx + 1, current_sum + track)

        # Гілка 2: пропускаємо поточний трек
        backtrack(idx + 1, current_sum)

    backtrack(0, 0)
    return best


def main() -> None:
    out = []
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue

        capacity = int(parts[0])
        count = int(parts[1])
        tracks = [int(x) for x in parts[2 : 2 + count]]

        best_sum = solve_cd(capacity, tracks)
        out.append(f"sum:{best_sum}")

    if out:
        sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
