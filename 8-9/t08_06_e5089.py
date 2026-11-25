import sys


def selection_sort_strings(words: list[str]) -> None:
    """Сортує список слів у лексикографічному порядку методом вибору."""
    n = len(words)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if words[j] < words[min_idx]:
                min_idx = j
        if min_idx != i:
            words[i], words[min_idx] = words[min_idx], words[i]


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    words = data[1 : n + 1]

    # Сортуємо слова словника методом вибору
    selection_sort_strings(words)

    sys.stdout.write("\n".join(words) + "\n")


if __name__ == "__main__":
    main()
