import sys


def tricky_key(x: int) -> tuple[int, int]:
    """Ключ сортування: спочатку остання цифра числа, потім саме число."""
    return (x % 10, x)


def insertion_sort_tricky(arr: list[int]) -> None:
    """Сортує масив методом вставки за останньою цифрою, а при рівності — за значенням."""
    for i in range(1, len(arr)):
        current = arr[i]
        current_key = tricky_key(current)
        j = i - 1
        while j >= 0 and tricky_key(arr[j]) > current_key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    arr = [int(x) for x in data[1 : n + 1]]

    # Виконуємо хитре сортування
    insertion_sort_tricky(arr)

    sys.stdout.write(" ".join(str(x) for x in arr) + "\n")


if __name__ == "__main__":
    main()
