import sys

# Знімаємо обмеження Python на кількість десяткових цифр при перетворенні str <-> int
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

# Поріг (у бітах), нижче якого виконується базове множення без подальшого розбиття
BASE_BITS = 1024


def karatsuba(x: int, y: int) -> int:
    """Множить два невід'ємних цілих числа x та y алгоритмом Карацуби."""
    if x == 0 or y == 0:
        return 0

    # Базовий випадок рекурсії
    if x.bit_length() <= BASE_BITS or y.bit_length() <= BASE_BITS:
        return x * y

    # Розбиваємо обидва числа на старшу та молодшу половини по половині бітової довжини
    half = max(x.bit_length(), y.bit_length()) >> 1
    mask = (1 << half) - 1

    x_low = x & mask
    x_high = x >> half
    y_low = y & mask
    y_high = y >> half

    # Три рекурсивні множення замість чотирьох:
    # x * y = z2 * 2^(2*half) + (z1 - z2 - z0) * 2^half + z0
    z0 = karatsuba(x_low, y_low)
    z2 = karatsuba(x_high, y_high)
    z1 = karatsuba(x_low + x_high, y_low + y_high) - z2 - z0

    return (z2 << (half << 1)) + (z1 << half) + z0


def main() -> None:
    data = sys.stdin.read().split()
    if len(data) < 2:
        return

    a = int(data[0])
    b = int(data[1])

    product = karatsuba(a, b)
    sys.stdout.write(f"{product}\n")


if __name__ == "__main__":
    main()
