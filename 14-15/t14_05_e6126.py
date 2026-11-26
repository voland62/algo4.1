import sys


class Node:
    """Вузол рекурсивної структури даних для реалізації черги."""

    __slots__ = ("value", "next")

    def __init__(self, value: int, next_node: "Node | None" = None) -> None:
        self.value = value
        self.next = next_node


class Queue:
    """Черга з захистом від помилок, реалізована як однозв'язний список."""

    def __init__(self) -> None:
        self._front: Node | None = None
        self._back: Node | None = None
        self._size: int = 0

    def push(self, value: int) -> str:
        """Додає елемент у кінець черги."""
        new_node = Node(value)
        if self._back is None:
            self._front = new_node
            self._back = new_node
        else:
            self._back.next = new_node
            self._back = new_node
        self._size += 1
        return "ok"

    def pop(self) -> str:
        """Видаляє та повертає перший елемент черги або 'error', якщо черга порожня."""
        if self._front is None:
            return "error"
        value = self._front.value
        self._front = self._front.next
        if self._front is None:
            # Якщо видалено останній вузол, обнуляємо і вказівник на хвіст
            self._back = None
        self._size -= 1
        return str(value)

    def front(self) -> str:
        """Повертає перший елемент черги без видалення або 'error', якщо черга порожня."""
        if self._front is None:
            return "error"
        return str(self._front.value)

    def size(self) -> str:
        """Повертає поточну кількість елементів у черзі."""
        return str(self._size)

    def clear(self) -> str:
        """Очищає чергу."""
        self._front = None
        self._back = None
        self._size = 0
        return "ok"


def main() -> None:
    """Зчитує команди зі стандартного вводу та моделює роботу черги."""
    queue = Queue()
    out = []

    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue

        cmd = parts[0]
        if cmd == "push":
            out.append(queue.push(int(parts[1])))
        elif cmd == "pop":
            out.append(queue.pop())
        elif cmd == "front":
            out.append(queue.front())
        elif cmd == "size":
            out.append(queue.size())
        elif cmd == "clear":
            out.append(queue.clear())
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
