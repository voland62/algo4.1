def f(x: float) -> float:
    """Функція f(x) = x^3 + 4x^2 + x - 6."""
    return x**3 + 4.0 * x**2 + x - 6.0


def find_root(left: float, right: float, eps: float = 1e-12) -> float:
    """Знаходить корінь рівняння f(x) = 0 на відрізку [left, right] методом бінарного пошуку."""
    # На відрізку [0, 2] похідна f'(x) = 3x^2 + 8x + 1 > 0,
    # тому функція строго зростає, причому f(0) = -6 < 0, f(2) = 20 > 0.
    while right - left > eps:
        mid = (left + right) / 2.0
        if f(mid) < 0.0:
            # Оскільки f(x) зростає і f(mid) < 0, корінь лежить правіше від mid
            left = mid
        else:
            # Якщо f(mid) >= 0, корінь лежить лівіше від mid або в самій точці mid
            right = mid

    return (left + right) / 2.0


def main() -> None:
    # Шукаємо корінь на заданому відрізку [0, 2]
    root = find_root(0.0, 2.0)

    # Виводимо знайдений корінь та перевірку підстановкою
    print(f"Корінь рівняння x^3 + 4x^2 + x - 6 = 0 на [0, 2]: x = {root:.10f}")
    print(f"Перевірка: f(x) = {f(root):.10f}")


if __name__ == "__main__":
    main()
