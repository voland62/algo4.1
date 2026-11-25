import sys


def lower_bound(colors: list[int], target: int) -> int:
    """Знаходить індекс першого елемента, не меншого за target (ліва межа входжень)."""
    left = 0
    right = len(colors)

    while left < right:
        mid = (left + right) // 2
        if colors[mid] < target:
            # Усі елементи до mid включно менші за target — зсуваємо ліву межу
            left = mid + 1
        else:
            # Елемент >= target — можливо, є підходящий елемент лівіше
            right = mid

    return left


def upper_bound(colors: list[int], target: int) -> int:
    """Знаходить індекс першого елемента, строго більшого за target (права межа входжень)."""
    left = 0
    right = len(colors)

    while left < right:
        mid = (left + right) // 2
        if colors[mid] <= target:
            # Усі елементи до mid включно <= target — зсуваємо ліву межу
            left = mid + 1
        else:
            # Елемент > target — шукаємо найперший такий елемент
            right = mid

    return left


def main() -> None:
    # Зчитуємо всі вхідні дані за один раз (коректно працює також при n = 0)
    data = sys.stdin.read().split()
    if not data:
        return

    # Зчитуємо кількість тварин та їхні кольори (відсортовані за неспаданням)
    n = int(data[0])
    colors = [int(x) for x in data[1 : n + 1]]

    # Зчитуємо кількість запитів та кольори для підрахунку
    m = int(data[n + 1])
    queries = [int(x) for x in data[n + 2 : n + 2 + m]]

    # Кількість входжень кольору k дорівнює різниці правої та лівої меж
    results = [
        str(upper_bound(colors, k) - lower_bound(colors, k))
        for k in queries
    ]

    # Виводимо відповіді по одній у рядку
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
