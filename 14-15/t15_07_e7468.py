import sys


class Node:
    """Вузол однозв'язного списку."""

    def __init__(self, data: int, next_node: "Node | None" = None) -> None:
        self.data: int = data
        self.next: Node | None = next_node


class List:
    """Однозв'язний список з вказівниками на голову та хвіст."""

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def addToTail(self, val: int) -> None:
        """Додає число val у кінець зв'язного списку."""
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def ReorderList(self) -> None:
        """Перевпорядковує список у порядку L0 -> Ln -> L1 -> L(n-1) -> ... без додаткової пам'яті."""
        if self.head is None or self.head.next is None or self.head.next.next is None:
            return

        # Крок 1: знаходимо середину списку методом повільного та швидкого вказівників
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Розділяємо список на першу та другу половини
        second_half = slow.next
        slow.next = None

        # Крок 2: розвертаємо другу половину списку ітеративно
        prev_node: Node | None = None
        current = second_half
        while current is not None:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        second_half = prev_node

        # Крок 3: почергово зливаємо вузли першої та розвернутої другої половин
        first_half = self.head
        new_tail = first_half
        while second_half is not None:
            next_first = first_half.next
            next_second = second_half.next

            first_half.next = second_half
            second_half.next = next_first
            new_tail = second_half if next_first is None else next_first

            first_half = next_first
            second_half = next_second

        self.tail = new_tail

    def Print(self) -> None:
        """Виводить елементи зв'язного списку через пробіл."""
        current = self.head
        first = True
        while current is not None:
            if not first:
                sys.stdout.write(" ")
            sys.stdout.write(str(current.data))
            first = False
            current = current.next
        sys.stdout.write("\n")


def main() -> None:
    """Зчитує вхідні дані, перевпорядковує зв'язний список та виводить його."""
    # Блок зчитування вхідних даних
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    linked_list = List()
    for i in range(1, n + 1):
        linked_list.addToTail(int(tokens[i]))

    # Перевпорядкування та виведення виключно через маніпуляцію вказівниками вузлів
    linked_list.ReorderList()
    linked_list.Print()


if __name__ == "__main__":
    main()
