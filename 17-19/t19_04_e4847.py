from __future__ import annotations

import sys


class PriorityQueue:
    """Черга з пріоритетами на базі максимальної двійкової купи з індексною мапою."""

    def __init__(self) -> None:
        self._priorities: list[int] = []
        self._ids: list[str] = []
        # Відображення id -> поточний індекс у купі для виконання CHANGE за O(log n)
        self._pos: dict[str, int] = {}

    def _swap(self, i: int, j: int) -> None:
        """Міняє місцями два елементи купи та оновлює індекси в мапі."""
        priorities = self._priorities
        ids = self._ids
        pos = self._pos

        id_i = ids[i]
        id_j = ids[j]
        priorities[i], priorities[j] = priorities[j], priorities[i]
        ids[i], ids[j] = id_j, id_i
        pos[id_i] = j
        pos[id_j] = i

    def _sift_up(self, idx: int) -> None:
        """Просіює елемент угору для відновлення властивості максимальної купи."""
        priorities = self._priorities
        while idx > 0:
            parent = (idx - 1) >> 1
            if priorities[idx] <= priorities[parent]:
                break
            self._swap(idx, parent)
            idx = parent

    def _sift_down(self, idx: int) -> None:
        """Просіює елемент униз для відновлення властивості максимальної купи."""
        priorities = self._priorities
        size = len(priorities)
        half = size >> 1
        while idx < half:
            left = (idx << 1) + 1
            right = left + 1
            best = left
            if right < size and priorities[right] > priorities[left]:
                best = right
            if priorities[idx] >= priorities[best]:
                break
            self._swap(idx, best)
            idx = best

    def add(self, item_id: str, priority: int) -> None:
        """Додає новий елемент у чергу з пріоритетами за O(log n)."""
        idx = len(self._ids)
        self._ids.append(item_id)
        self._priorities.append(priority)
        self._pos[item_id] = idx
        self._sift_up(idx)

    def pop(self) -> tuple[str, int]:
        """Видаляє і повертає елемент з найбільшим пріоритетом за O(log n)."""
        top_id = self._ids[0]
        top_priority = self._priorities[0]
        last_idx = len(self._ids) - 1
        if last_idx > 0:
            self._swap(0, last_idx)
        self._ids.pop()
        self._priorities.pop()
        del self._pos[top_id]
        if self._ids:
            self._sift_down(0)
        return top_id, top_priority

    def change(self, item_id: str, new_priority: int) -> None:
        """Змінює пріоритет елемента item_id на new_priority за O(log n)."""
        idx = self._pos[item_id]
        old_priority = self._priorities[idx]
        self._priorities[idx] = new_priority
        if new_priority > old_priority:
            self._sift_up(idx)
        elif new_priority < old_priority:
            self._sift_down(idx)


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    pq = PriorityQueue()
    out: list[str] = []
    i = 0
    total = len(tokens)

    while i < total:
        cmd = tokens[i]
        if cmd == b"ADD":
            item_id = tokens[i + 1].decode()
            priority = int(tokens[i + 2])
            pq.add(item_id, priority)
            i += 3
        elif cmd == b"POP":
            item_id, priority = pq.pop()
            out.append(f"{item_id} {priority}")
            i += 1
        elif cmd == b"CHANGE":
            item_id = tokens[i + 1].decode()
            new_priority = int(tokens[i + 2])
            pq.change(item_id, new_priority)
            i += 3
        else:
            i += 1

    if out:
        sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
