import sys


def bubble_sort_swaps(arr: list[int]) -> int:
    """Сортує масив методом бульбашки та повертає кількість виконаних обмінів."""
    n = len(arr)
    swaps = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Міняємо сусідні елементи місцями та збільшуємо лічильник обмінів
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return swaps


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    arr = [int(x) for x in data[1 : n + 1]]

    # Виводимо кількість обмінів під час сортування бульбашкою
    sys.stdout.write(f"{bubble_sort_swaps(arr)}\n")


if __name__ == "__main__":
    main()
