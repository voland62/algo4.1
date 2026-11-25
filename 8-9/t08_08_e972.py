import sys


def insertion_sort(items: list[tuple[int, int, int]]) -> None:
    """Сортує список моментів часу (h, m, s) за неспаданням методом вставки."""
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        # Зсуваємо більші моменти часу вправо
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    times = []
    idx = 1
    for _ in range(n):
        h = int(data[idx])
        m = int(data[idx + 1])
        s = int(data[idx + 2])
        times.append((h, m, s))
        idx += 3

    # Сортуємо моменти часу методом вставки
    insertion_sort(times)

    # Виводимо відсортовані моменти часу по одному в рядку
    out = [f"{h} {m} {s}" for h, m, s in times]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
