import math
import sys


def solve_equation(c: float) -> float:
    """Знаходить корінь рівняння x^2 + sqrt(x) = c методом бінарного пошуку."""
    # Функція f(x) = x^2 + sqrt(x) строго зростає на [0, +∞)
    # Оскільки при x = sqrt(c) маємо f(sqrt(c)) = c + c^(1/4) > c,
    # корінь гарантовано лежить на відрізку [0, sqrt(c)]
    left = 0.0
    right = math.sqrt(c)

    # 100 ітерацій зменшують довжину відрізка у 2^100 разів —
    # цього з запасом вистачає для максимальної точності типу float
    for _ in range(100):
        mid = (left + right) / 2.0
        if mid * mid + math.sqrt(mid) < c:
            # Значення функції менше за c — шуканий корінь правіше
            left = mid
        else:
            # Значення функції >= c — шуканий корінь лівіше або в mid
            right = mid

    return (left + right) / 2.0


def main() -> None:
    # Зчитуємо вхідне дійсне число C
    data = sys.stdin.read().split()
    if not data:
        return

    c = float(data[0])
    answer = solve_equation(c)

    # Виводимо результат із точністю 10 знаків після коми (вимога — не менше 6)
    sys.stdout.write(f"{answer:.10f}\n")


if __name__ == "__main__":
    main()
