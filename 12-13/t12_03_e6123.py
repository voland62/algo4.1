import sys


class Node:
    """Вузол рекурсивної структури даних для реалізації стеку."""

    def __init__(self, value: int, next_node: "Node | None" = None) -> None:
        self.value = value
        self.next = next_node


class Stack:
    """Стек із захистом від помилок, реалізований як рекурсивна структура (однозв'язний список)."""

    def __init__(self) -> None:
        self._top: Node | None = None
        self._size: int = 0

    def push(self, value: int) -> str:
        """Додає елемент на вершину стеку."""
        self._top = Node(value, self._top)
        self._size += 1
        return "ok"

    def pop(self) -> str:
        """Видаляє та повертає верхній елемент стеку або 'error', якщо стек порожній."""
        if self._top is None:
            return "error"
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return str(value)

    def back(self) -> str:
        """Повертає верхній елемент стеку без видалення або 'error', якщо стек порожній."""
        if self._top is None:
            return "error"
        return str(self._top.value)

    def size(self) -> str:
        """Повертає поточну кількість елементів у стеку."""
        return str(self._size)

    def clear(self) -> str:
        """Очищає стек."""
        self._top = None
        self._size = 0
        return "ok"


def main() -> None:
    stack = Stack()
    out = []

    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue

        cmd = parts[0]
        if cmd == "push":
            out.append(stack.push(int(parts[1])))
        elif cmd == "pop":
            out.append(stack.pop())
        elif cmd == "back":
            out.append(stack.back())
        elif cmd == "size":
            out.append(stack.size())
        elif cmd == "clear":
            out.append(stack.clear())
        elif cmd == "exit":
            out.append("bye")
            break

    if out:
        sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
