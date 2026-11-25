import sys


def generate_permutations(
    n: int,
    k: int,
    current: list[str],
    used: list[bool],
    output: list[str],
) -> None:
    """Рекурсивно генерує всі k-перестановки з чисел 1..n у лексикографічному порядку."""
    if len(current) == k:
        output.append(" ".join(current))
        return

    # Перебираємо числа від 1 до n по порядку для збереження лексикографічного порядку
    for num in range(1, n + 1):
        if not used[num]:
            used[num] = True
            current.append(str(num))
            generate_permutations(n, k, current, used, output)
            current.pop()
            used[num] = False


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    k = int(data[1])

    used = [False] * (n + 1)
    output = []
    generate_permutations(n, k, [], used, output)

    if output:
        sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
