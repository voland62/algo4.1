import sys


def selection_sort_first_moves(arr: list[int]) -> int:
    """Сортує масив методом вибору (мінімуму) та рахує переміщення початкового першого елемента."""
    n = len(arr)
    # Відстежуємо поточний індекс елемента, який спочатку стояв на позиції 0
    first_pos = 0
    moves = 0

    for i in range(n - 1):
        # Знаходимо індекс мінімального елемента на відрізку [i, n - 1]
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Якщо мінімум не на позиції i, виконуємо обмін
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            # Перевіряємо, чи брав участь у цьому обміні початковий перший елемент
            if first_pos == i:
                first_pos = min_idx
                moves += 1
            elif first_pos == min_idx:
                first_pos = i
                moves += 1

    return moves


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    arr = [int(x) for x in data[1 : n + 1]]

    # Виводимо кількість переміщень першого елемента
    sys.stdout.write(f"{selection_sort_first_moves(arr)}\n")


if __name__ == "__main__":
    main()
