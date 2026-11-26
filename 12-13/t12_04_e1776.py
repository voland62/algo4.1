import sys


def can_reorder(n: int, target: list[int]) -> bool:
    """Перевіряє за допомогою стеку (тупика), чи можна отримати перестановку вагонів target."""
    station_stack = []
    next_car = 1

    for needed in target:
        # Заганяємо вагони з напрямку A у тупик, доки на вершині не з'явиться потрібний вагон
        while next_car <= n and (not station_stack or station_stack[-1] != needed):
            station_stack.append(next_car)
            next_car += 1

        # Якщо на вершині тупика потрібний вагон — відправляємо його у напрямок B
        if station_stack and station_stack[-1] == needed:
            station_stack.pop()
        else:
            return False

    return True


def main() -> None:
    lines = sys.stdin.read().splitlines()
    idx = 0
    total_lines = len(lines)
    out = []

    while idx < total_lines:
        line = lines[idx].strip()
        idx += 1
        if not line:
            continue

        n = int(line)
        if n == 0:
            # Завершальний нульовий блок
            break

        # Обробляємо всі перестановки поточного блоку до рядка '0'
        while idx < total_lines:
            perm_line = lines[idx].strip()
            idx += 1
            if not perm_line:
                continue

            nums = [int(x) for x in perm_line.split()]
            if nums[0] == 0:
                # Порожній рядок після кожного блоку
                out.append("")
                break

            out.append("Yes" if can_reorder(n, nums) else "No")

    if out:
        sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
