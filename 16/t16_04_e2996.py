import sys

sys.setrecursionlimit(20000)


class TreeNode:
    """Вузол дерева підпорядкування співробітників (рекурсивна структура)."""

    def __init__(self, node_id: int, fee: int = 0) -> None:
        self.node_id = node_id
        self.fee = fee
        self.children: list[TreeNode] = []

    def add_child(self, child: "TreeNode") -> None:
        """Додає безпосереднього підлеглого до списку дітей поточного вузла."""
        self.children.append(child)


def min_approval_cost(node: TreeNode) -> int:
    """Рекурсивно обчислює мінімальну суму офіційних зборів від листка до поточного вузла."""
    if not node.children:
        return node.fee
    best_subordinate_cost = min(min_approval_cost(child) for child in node.children)
    return node.fee + best_subordinate_cost


def main() -> None:
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))

    # Попередньо створюємо всі вузли, щоб коректно пов'язати дерево незалежно від порядку ID
    nodes = [TreeNode(i) for i in range(n + 1)]

    for employee_id in range(1, n + 1):
        fee = int(next(it))
        k = int(next(it))
        nodes[employee_id].fee = fee
        for _ in range(k):
            subordinate_id = int(next(it))
            nodes[employee_id].add_child(nodes[subordinate_id])

    # Директор завжди має номер 1 і є коренем дерева
    print(min_approval_cost(nodes[1]))


if __name__ == "__main__":
    main()
