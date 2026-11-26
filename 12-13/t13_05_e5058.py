import sys


def is_valid_brackets(seq: str) -> bool:
    """Перевіряє коректність дужкової послідовності з (), [], {} за допомогою стеку."""
    stack = []
    # Відповідність закриваючих дужок відкриваючим
    matching = {")": "(", "]": "[", "}": "{"}

    for ch in seq:
        if ch in "([{":
            stack.append(ch)
        elif ch in matching:
            # Якщо стек порожній або верхня дужка не відповідає поточній закриваючій
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()

    # Послідовність правильна, якщо всі відкриті дужки були закриті
    return len(stack) == 0


def main() -> None:
    line = sys.stdin.readline().strip()
    sys.stdout.write("yes\n" if is_valid_brackets(line) else "no\n")


if __name__ == "__main__":
    main()
