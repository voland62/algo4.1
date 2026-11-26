from __future__ import annotations

import sys

sys.setrecursionlimit(2000)


class Node:
    """Вузол бінарного дерева пошуку (рекурсивна структура)."""

    __slots__ = ("val", "left", "right")

    def __init__(
        self,
        val: int,
        left: Node | None = None,
        right: Node | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Tree:
    """Бінарне дерево пошуку."""

    def __init__(self) -> None:
        self.head: Node | None = None

    def insert(self, val: int) -> None:
        """Вставляє число val у бінарне дерево пошуку."""
        self.head = self._insert(self.head, val)

    def _insert(self, node: Node | None, val: int) -> Node:
        """Рекурсивно вставляє значення у відповідне піддерево."""
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            # Якщо значення дорівнює поточній вершині, вставляємо в праве піддерево
            node.right = self._insert(node.right, val)
        return node

    def is_same_tree(self, other: Tree) -> int:
        """Повертає 1, якщо поточне дерево ідентичне дереву other, інакше 0."""
        return 1 if self._is_same_node(self.head, other.head) else 0

    def _is_same_node(self, a: Node | None, b: Node | None) -> bool:
        """Рекурсивно перевіряє збіг структури та значень у двох піддеревах."""
        if a is None or b is None:
            return a is b
        return (
            a.val == b.val
            and self._is_same_node(a.left, b.left)
            and self._is_same_node(a.right, b.right)
        )


def main() -> None:
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    tree1 = Tree()
    for _ in range(n):
        tree1.insert(int(next(it)))

    m = int(next(it))
    tree2 = Tree()
    for _ in range(m):
        tree2.insert(int(next(it)))

    sys.stdout.write(f"{tree1.is_same_tree(tree2)}\n")


if __name__ == "__main__":
    main()
