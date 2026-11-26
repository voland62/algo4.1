import sys


class Node:
    """Вузол двозв'язного списку."""

    def __init__(
        self,
        data: int,
        prev_node: "Node | None" = None,
        next_node: "Node | None" = None,
    ) -> None:
        self.data: int = data
        self.prev: Node | None = prev_node
        self.next: Node | None = next_node


class List:
    """Двозв'язний список з вказівниками на голову та хвіст."""

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def addToTail(self, val: int) -> None:
        """Додає число val у кінець зв'язного списку."""
        new_node = Node(val, prev_node=self.tail)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        """Виводить елементи зв'язного списку у прямому порядку."""
        current = self.head
        first = True
        while current is not None:
            if not first:
                sys.stdout.write(" ")
            sys.stdout.write(str(current.data))
            first = False
            current = current.next
        sys.stdout.write("\n")

    def PrintReverse(self) -> None:
        """Виводить елементи зв'язного списку у зворотному порядку."""
        current = self.tail
        first = True
        while current is not None:
            if not first:
                sys.stdout.write(" ")
            sys.stdout.write(str(current.data))
            first = False
            current = current.prev
        sys.stdout.write("\n")


def main() -> None:
    """Зчитує вхідні дані, будує двозв'язний список та виводить його в обох напрямках."""
    # Блок зчитування вхідних даних
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    linked_list = List()
    for i in range(1, n + 1):
        linked_list.addToTail(int(tokens[i]))

    # Прямий та зворотний обхід без використання масивів чи словників
    linked_list.Print()
    linked_list.PrintReverse()


if __name__ == "__main__":
    main()
