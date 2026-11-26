from __future__ import annotations

import sys


def is_min_heap(arr: list[int], n: int) -> bool:
    """Перевіряє властивість мінімальної двійкової купи для масиву з 1-індексацією."""
    for i in range(1, n // 2 + 1):
        left = i << 1
        if left <= n and arr[i] > arr[left]:
            return False
        right = left + 1
        if right <= n and arr[i] > arr[right]:
            return False
    return True


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    # Додаємо фіктивний елемент на позицію 0 для прямої 1-індексації за умовою задачі
    arr = [0]
    arr.extend(map(int, tokens[1 : n + 1]))

    sys.stdout.write("YES\n" if is_min_heap(arr, n) else "NO\n")


if __name__ == "__main__":
    main()
