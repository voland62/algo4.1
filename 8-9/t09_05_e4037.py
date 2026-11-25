import sys


def merge_sort(robots: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Стійке сортування злиттям списку роботів (основний номер, допоміжний номер)."""
    n = len(robots)
    if n <= 1:
        return robots

    # Ітеративне (висхідне) сортування злиттям для високої швидкодії на великих N
    src = robots
    dst = [None] * n
    width = 1

    while width < n:
        for left in range(0, n, 2 * width):
            mid = min(left + width, n)
            right = min(left + 2 * width, n)

            i = left
            j = mid
            k = left

            # Злиття двох відсортованих підмасивів зі збереженням стійкості (<=)
            while i < mid and j < right:
                if src[i][0] <= src[j][0]:
                    dst[k] = src[i]
                    i += 1
                else:
                    dst[k] = src[j]
                    j += 1
                k += 1

            while i < mid:
                dst[k] = src[i]
                i += 1
                k += 1

            while j < right:
                dst[k] = src[j]
                j += 1
                k += 1

        # Міняємо місцями буфери після проходу
        src, dst = dst, src
        width *= 2

    return src


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    robots = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]

    # Сортуємо роботів стійким алгоритмом сортування злиттям
    sorted_robots = merge_sort(robots)

    out = [f"{a} {b}" for a, b in sorted_robots]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
