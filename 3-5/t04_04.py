import math


def f(x: float) -> float:
    """Функція f(x) = sin(x) - x / 3, нуль якої є коренем рівняння sin(x) = x / 3."""
    return math.sin(x) - x / 3.0


def find_root(left: float, right: float, eps: float = 1e-12) -> float:
    """Знаходить корінь рівняння f(x) = 0 на відрізку [left, right] методом бінарного пошуку."""
    # На відрізку [1.6, 3] (де pi/2 < 1.6 та 3 < pi) функція sin(x) спадає,
    # а x / 3 зростає, тому f(x) = sin(x) - x / 3 є строго спадною:
    # f(1.6) > 0, f(3) < 0.
    while right - left > eps:
        mid = (left + right) / 2.0
        if f(mid) > 0.0:
            # Оскільки f(x) спадає і f(mid) > 0, корінь лежить правіше від mid
            left = mid
        else:
            # Якщо f(mid) <= 0, корінь лежить лівіше від mid або в самій точці mid
            right = mid

    return (left + right) / 2.0


def main() -> None:
    # Шукаємо корінь на заданому відрізку [1.6, 3]
    root = find_root(1.6, 3.0)

    # Виводимо знайдений корінь та перевірку підстановкою
    print(f"Корінь рівняння sin(x) = x / 3 на [1.6, 3]: x = {root:.10f}")
    print(f"Перевірка: sin(x) = {math.sin(root):.10f}, x / 3 = {root / 3.0:.10f}")


if __name__ == "__main__":
    main()
