import sys


class Node:
    """Вузол рекурсивної структури даних для реалізації двосторонньої черги."""

    __slots__ = ("value", "prev", "next")

    def __init__(
        self,
        value: int,
        prev_node: "Node | None" = None,
        next_node: "Node | None" = None,
    ) -> None:
        self.value = value
        self.prev = prev_node
        self.next = next_node


class Deque:
    """Дек необмеженого розміру, реалізований як двозв'язний список."""

    def __init__(self) -> None:
        self._front: Node | None = None
        self._back: Node | None = None
        self._size: int = 0

    def push_front(self, value: int) -> str:
        """Додає елемент на початок дека."""
        new_node = Node(value, None, self._front)
        if self._front is None:
            self._front = new_node
            self._back = new_node
        else:
            self._front.prev = new_node
            self._front = new_node
        self._size += 1
        return "ok"

    def push_back(self, value: int) -> str:
        """Додає елемент у кінець дека."""
        new_node = Node(value, self._back, None)
        if self._back is None:
            self._front = new_node
            self._back = new_node
        else:
            self._back.next = new_node
            self._back = new_node
        self._size += 1
        return "ok"

    def pop_front(self) -> str:
        """Видаляє та повертає перший елемент дека або 'error', якщо дек порожній."""
        if self._front is None:
            return "error"
        value = self._front.value
        self._front = self._front.next
        if self._front is None:
            self._back = None
        else:
            self._front.prev = None
        self._size -= 1
        return str(value)

    def pop_back(self) -> str:
        """Видаляє та повертає останній елемент дека або 'error', якщо дек порожній."""
        if self._back is None:
            return "error"
        value = self._back.value
        self._back = self._back.prev
        if self._back is None:
            self._front = None
        else:
            self._back.next = None
        self._size -= 1
        return str(value)

    def front(self) -> str:
        """Повертає перший елемент дека без видалення або 'error', якщо дек порожній."""
        if self._front is None:
            return "error"
        return str(self._front.value)

    def back(self) -> str:
        """Повертає останній елемент дека без видалення або 'error', якщо дек порожній."""
        if self._back is None:
            return "error"
        return str(self._back.value)

    def size(self) -> str:
        """Повертає поточну кількість елементів у деку."""
        return str(self._size)

    def clear(self) -> str:
        """Видаляє всі елементи з дека, розриваючи циклічні посилання."""
        current = self._front
        while current is not None:
            nxt = current.next
            current.prev = None
            current.next = None
            current = nxt
        self._front = None
        self._back = None
        self._size = 0
        return "ok"


def main() -> None:
    """Зчитує команди зі стандартного вводу та моделює роботу дека."""
    deque = Deque()
    out = []

    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue

        cmd = parts[0]
        if cmd == "push_front":
            out.append(deque.push_front(int(parts[1])))
        elif cmd == "push_back":
            out.append(deque.push_back(int(parts[1])))
        elif cmd == "pop_front":
            out.append(deque.pop_front())
        elif cmd == "pop_back":
            out.append(deque.pop_back())
        elif cmd == "front":
            out.append(deque.front())
        elif cmd == "back":
            out.append(deque.back())
        elif cmd == "size":
            out.append(deque.size())
        elif cmd == "clear":
            out.append(deque.clear())
        elif cmd == "exit":
            out.append("bye")
            break

        if len(out) >= 8192:
            sys.stdout.write("\n".join(out) + "\n")
            out.clear()

    if out:
        sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
