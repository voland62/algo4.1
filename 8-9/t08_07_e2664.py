import sys


def library_insertion_sort(arr: list[int]) -> list[str]:
    """Виконує сортування вставкою та зберігає стан масиву після кожного кроку зі зміною."""
    steps = []
    n = len(arr)

    for i in range(1, n):
        current = arr[i]
        j = i - 1
        moved = False

        # Зсуваємо елементи, більші за current, вправо
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
            moved = True

        arr[j + 1] = current

        # Виводимо стан масиву лише якщо поточний елемент змінив свою позицію
        if moved:
            steps.append(" ".join(str(x) for x in arr))

    return steps


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    arr = [int(x) for x in data[1 : n + 1]]

    steps = library_insertion_sort(arr)
    if steps:
        sys.stdout.write("\n".join(steps) + "\n")


if __name__ == "__main__":
    main()
