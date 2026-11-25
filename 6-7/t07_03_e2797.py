import sys


class HashSet:
    """Хеш-таблиця з відкритою адресацією (лінійне зондування) для цілих чисел."""

    def __init__(self, capacity: int = 262144) -> None:
        # Розмір таблиці — степінь двійки (2^18 = 262144), що при N <= 10^5
        # забезпечує коефіцієнт заповнення < 0.39 без потреби рехешування
        self._mask = capacity - 1
        self._table = [None] * capacity
        self._count = 0

    def add_all(self, numbers) -> None:
        """Додає послідовність цілих чисел до хеш-таблиці."""
        table = self._table
        mask = self._mask
        count = self._count

        for key in numbers:
            # Власна мультиплікативна хеш-функція Кнута (без вбудованої hash())
            idx = ((key * 2654435761) >> 14) & mask
            while True:
                cur = table[idx]
                if cur is None:
                    # Вільна комірка — записуємо новий унікальний номер
                    table[idx] = key
                    count += 1
                    break
                if cur == key:
                    # Номер уже є в контактній книзі
                    break
                # Колізія — переходимо до наступної комірки
                idx = (idx + 1) & mask

        self._count = count

    def size(self) -> int:
        """Повертає кількість унікальних елементів у хеш-таблиці."""
        return self._count


def main() -> None:
    # Зчитуємо всі вхідні дані за один раз
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    contacts = HashSet()

    # Додаємо всі телефонні номери у хеш-таблицю
    contacts.add_all(map(int, data[1 : n + 1]))

    # Виводимо кількість унікальних контактів
    sys.stdout.write(f"{contacts.size()}\n")


if __name__ == "__main__":
    main()
