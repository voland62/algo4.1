from __future__ import annotations

import sys


class MaxBinaryHeap:
    """Максимальна двійкова купа для реалізації пірамідального сортування (Heap Sort)."""

    def __init__(self, data: list[int]) -> None:
        self._data = data
        self._size = len(data)
        # Побудова максимальної купи знизу вгору за лінійний час O(n)
        for idx in range((self._size >> 1) - 1, -1, -1):
            self._sift_down(idx, self._size)

    def _sift_down(self, idx: int, size: int) -> None:
        """Просіює елемент униз у межах купи розміром size."""
        data = self._data
        root_val = data[idx]
        half = size >> 1
        while idx < half:
            child = (idx << 1) + 1
            right = child + 1
            if right < size and data[right] > data[child]:
                child = right
            if root_val >= data[child]:
                break
            data[idx] = data[child]
            idx = child
        data[idx] = root_val

    def sort(self) -> list[int]:
        """Сортує елементи у неспадному порядку за O(n log n)."""
        data = self._data
        for end in range(self._size - 1, 0, -1):
            data[0], data[end] = data[end], data[0]
            self._sift_down(0, end)
        self._size = 0
        return data


def main() -> None:
    raw_tokens = sys.stdin.buffer.read().split()
    if not raw_tokens:
        return

    nums = list(map(int, raw_tokens))
    sorted_nums = MaxBinaryHeap(nums).sort()
    sys.stdout.write(" ".join(map(str, sorted_nums)) + "\n")


if __name__ == "__main__":
    main()
