import sys

sys.setrecursionlimit(20000)


class DirNode:
    """Вузол дерева каталогів (рекурсивна структура з економією пам'яті)."""

    __slots__ = ("name", "children")

    def __init__(self, name: str = "") -> None:
        self.name = name
        # Відкладаємо виділення списку дітей до появи першого підкаталогу
        self.children: list[DirNode] | None = None

    def insert_path(self, parts: list[str], index: int = 0) -> None:
        """Рекурсивно додає складові шляху до дерева каталогів."""
        if index >= len(parts):
            return
        part = parts[index]
        if self.children is None:
            self.children = []

        for child in self.children:
            if child.name == part:
                child.insert_path(parts, index + 1)
                return

        child = DirNode(part)
        self.children.append(child)
        child.insert_path(parts, index + 1)

    def print_tree(self, depth: int = -1) -> None:
        """Рекурсивно виводить дерево каталогів у лексикографічному порядку."""
        if depth >= 0:
            sys.stdout.write(" " * depth + self.name + "\n")
        if self.children is None:
            return
        self.children.sort(key=lambda child: child.name)
        for child in self.children:
            child.print_tree(depth + 1)


def main() -> None:
    n: int | None = None
    processed = 0
    # Віртуальний корінь на глибині -1, щоб кореневі каталоги мали глибину 0 (без пропусків)
    root = DirNode()

    for raw_line in sys.stdin:
        line = raw_line.rstrip("\r\n")
        if not line.strip():
            continue
        if n is None:
            n = int(line.strip())
            continue
        root.insert_path(line.split("\\"))
        processed += 1
        if processed == n:
            break

    if n is not None:
        root.print_tree(-1)


if __name__ == "__main__":
    main()
