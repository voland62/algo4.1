import sys


def quick_sort(arr: list[int], left: int, right: int) -> None:
    """Сортує відрізок масиву [left, right] алгоритмом швидкого сортування (Hoare partition)."""
    if left >= right:
        return

    # Обираємо опорний елемент із середини відрізка
    pivot = arr[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # Рекурсивно сортуємо ліву та праву частини
    if left < j:
        quick_sort(arr, left, j)
    if i < right:
        quick_sort(arr, i, right)


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    arr = [int(x) for x in data[1 : n + 1]]

    # Виконуємо швидке сортування
    if n > 1:
        quick_sort(arr, 0, n - 1)

    sys.stdout.write(" ".join(str(x) for x in arr) + "\n")


if __name__ == "__main__":
    main()
