import sys


def prefix_to_infix(expr: str) -> str:
    """Перетворює префіксний вираз у інфіксний з мінімальною кількістю дужок за допомогою стеку."""
    # Пріоритети операцій: + та - мають пріоритет 1, * та / мають пріоритет 2, операнди — 3
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    # Стек зберігає пари (інфіксний_підвираз, пріоритет_його_головної_операції)
    stack: list[tuple[str, int]] = []

    # Проходимо префіксний вираз справа наліво
    for ch in reversed(expr):
        if ch in precedence:
            op_prec = precedence[ch]
            left_expr, left_prec = stack.pop()
            right_expr, right_prec = stack.pop()

            # Лівий операнд потребує дужок лише якщо його пріоритет строго менший
            if left_prec < op_prec:
                left_expr = f"({left_expr})"

            # Правий операнд потребує дужок, якщо його пріоритет менший,
            # або рівний при некомутативній/лівоасоціативній операції '-' чи '/'
            if right_prec < op_prec or (right_prec == op_prec and ch in "-/"):
                right_expr = f"({right_expr})"

            stack.append((f"{left_expr}{ch}{right_expr}", op_prec))
        else:
            # Операнд (мала латинська літера) має найвищий пріоритет і не потребує дужок
            stack.append((ch, 3))

    return stack[-1][0]


def main() -> None:
    expr = sys.stdin.read().strip()
    if not expr:
        return

    sys.stdout.write(prefix_to_infix(expr) + "\n")


if __name__ == "__main__":
    main()
