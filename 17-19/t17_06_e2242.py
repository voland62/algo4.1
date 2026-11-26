from __future__ import annotations

import sys

sys.setrecursionlimit(20000)


class Node:
    """Вузол бінарного дерева пошуку (рекурсивна структура)."""

    __slots__ = ("val", "left", "right")

    def __init__(
        self,
        val: str,
        left: Node | None = None,
        right: Node | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def insert(node: Node | None, val: str) -> Node:
    """Рекурсивно вставляє літерну позначку в бінарне дерево пошуку."""
    if node is None:
        return Node(val)
    if val < node.val:
        node.left = insert(node.left, val)
    elif val > node.val:
        node.right = insert(node.right, val)
    return node


def preorder(node: Node | None, out: list[str]) -> None:
    """Рекурсивно виконує прямий обхід дерева (корінь, ліве, праве піддерево)."""
    if node is None:
        return
    out.append(node.val)
    preorder(node.left, out)
    preorder(node.right, out)


def main() -> None:
    rows: list[str] = []
    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue
        if line == "*":
            break
        rows.append(line)

    root: Node | None = None
    # Відновлюємо дерево у зворотному порядку зняття листків: від кореня до нижніх рівнів
    for row in reversed(rows):
        for ch in row:
            if not ch.isspace():
                root = insert(root, ch)

    if root is not None:
        out: list[str] = []
        preorder(root, out)
        sys.stdout.write("".join(out) + "\n")


if __name__ == "__main__":
    main()
