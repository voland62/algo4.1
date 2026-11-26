import sys

sys.setrecursionlimit(20000)


class GameNode:
    """Вузол дерева гри для двох гравців (рекурсивна структура)."""

    def __init__(self, node_id: int, value: int | None = None) -> None:
        self.node_id = node_id
        self.value = value
        self.children: list[GameNode] = []

    def add_child(self, child: "GameNode") -> None:
        """Додає нащадка (наступний хід) до поточного вузла дерева гри."""
        self.children.append(child)


def evaluate_game(node: GameNode, is_first_player: bool) -> int:
    """Рекурсивно обчислює підсумок гри за алгоритмом мінімакс при оптимальній грі."""
    if node.value is not None:
        return node.value
    if not node.children:
        return 0

    if is_first_player:
        # Перший гравець прагне максимізувати результат (+1 > 0 > -1)
        return max(evaluate_game(child, False) for child in node.children)
    # Другий гравець прагне мінімізувати результат (-1 < 0 < +1)
    return min(evaluate_game(child, True) for child in node.children)


def main() -> None:
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))

    # Попередньо створюємо всі вузли, оскільки батьківський вузол може мати довільний номер
    nodes = [GameNode(i) for i in range(n + 1)]

    for node_id in range(2, n + 1):
        node_type = next(it)
        parent_id = int(next(it))
        if node_type == "L":
            nodes[node_id].value = int(next(it))
        nodes[parent_id].add_child(nodes[node_id])

    # Корінь дерева має номер 1, гру завжди починає перший гравець
    result = evaluate_game(nodes[1], True)
    print("+1" if result == 1 else str(result))


if __name__ == "__main__":
    main()
