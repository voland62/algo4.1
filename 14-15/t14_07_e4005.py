import sys


class Node:
    """Вузол однозв'язного списку для моделювання колоди карт у вигляді черги."""

    __slots__ = ("value", "next")

    def __init__(self, value: int, next_node: "Node | None" = None) -> None:
        self.value = value
        self.next = next_node


class Queue:
    """Черга на основі однозв'язного списку з підтримкою переміщення вузлів."""

    def __init__(self) -> None:
        self._front: Node | None = None
        self._back: Node | None = None

    def is_empty(self) -> bool:
        """Перевіряє, чи черга порожня."""
        return self._front is None

    def enqueue(self, value: int) -> None:
        """Додає нове значення в кінець черги."""
        self.enqueue_node(Node(value))

    def enqueue_node(self, node: Node) -> None:
        """Додає існуючий вузол у кінець черги (без зайвих алокацій)."""
        node.next = None
        if self._back is None:
            self._front = node
            self._back = node
        else:
            self._back.next = node
            self._back = node

    def dequeue_node(self) -> Node:
        """Вилучає та повертає перший вузол із черги."""
        node = self._front
        self._front = node.next
        if self._front is None:
            self._back = None
        return node


def play_drunkard(first_deck: Queue, second_deck: Queue, n: int) -> str:
    """Моделює гру 'П'яниця' та повертає результат або 'draw' після 200000 ходів."""
    max_card = n - 1
    max_moves = 200_000
    moves = 0

    while not first_deck.is_empty() and not second_deck.is_empty() and moves < max_moves:
        node1 = first_deck.dequeue_node()
        node2 = second_deck.dequeue_node()
        c1 = node1.value
        c2 = node2.value

        # Карта 0 перемагає найбільшу карту (n - 1); в інших випадках перемагає більша
        if (c1 == 0 and c2 == max_card) or (c1 > c2 and not (c1 == max_card and c2 == 0)):
            winner = first_deck
        else:
            winner = second_deck

        # Переможець спочатку кладе під низ карту першого гравця, потім — другого
        winner.enqueue_node(node1)
        winner.enqueue_node(node2)
        moves += 1

    if first_deck.is_empty():
        return f"second {moves}"
    if second_deck.is_empty():
        return f"first {moves}"
    return "draw"


def main() -> None:
    """Зчитує колоди обох гравців та виводить переможця і кількість ходів."""
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    half = n // 2

    first_deck = Queue()
    second_deck = Queue()

    for i in range(1, half + 1):
        first_deck.enqueue(int(tokens[i]))
    for i in range(half + 1, n + 1):
        second_deck.enqueue(int(tokens[i]))

    # Звільняємо буфер вхідних токенів перед моделюванням довгої гри
    del tokens

    sys.stdout.write(play_drunkard(first_deck, second_deck, n) + "\n")


if __name__ == "__main__":
    main()
