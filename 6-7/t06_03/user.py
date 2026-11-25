"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
Реалізація на основі хеш-таблиці з відкритою адресацією (подвійне хешування).
"""

# Спеціальне значення-маркер для позначення видаленої комірки (tombstone)
_DELETED = object()

# Глобальні змінні хеш-таблиці
_size = 0           # Поточний розмір таблиці (просте число)
_count = 0          # Кількість активних авторів у таблиці
_deleted_count = 0  # Кількість видалених комірок (маркерів _DELETED)
_keys = []          # Масив ключів (імена авторів)
_values = []        # Масив значень (відсортовані списки назв книг автора)


def _is_prime(n: int) -> bool:
    """Перевіряє, чи є число n простим."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def _next_prime(n: int) -> int:
    """Знаходить найменше просте число, не менше за n."""
    if n <= 2:
        return 2
    candidate = n if n % 2 == 1 else n + 1
    while not _is_prime(candidate):
        candidate += 2
    return candidate


def _hash_string(key: str) -> int:
    """Поліноміальна хеш-функція для рядка."""
    h = 0
    for ch in key:
        h = (h * 131 + ord(ch)) & 0x7FFFFFFF
    return h


def _probe_params(key: str, table_size: int) -> tuple[int, int]:
    """Обчислює початковий індекс та крок для подвійного хешування."""
    h = _hash_string(key)
    start = h % table_size
    # Оскільки table_size — просте число, крок у [1, table_size - 1]
    # гарантує обхід усіх комірок таблиці
    step = 1 + (h % (table_size - 1))
    return start, step


def _rehash(new_size: int) -> None:
    """Перебудовує хеш-таблицю з новим розміром new_size, очищуючи видалені комірки."""
    global _size, _count, _deleted_count, _keys, _values

    old_keys = _keys
    old_values = _values

    _size = _next_prime(new_size)
    _keys = [None] * _size
    _values = [None] * _size
    _count = 0
    _deleted_count = 0

    for i in range(len(old_keys)):
        key = old_keys[i]
        if key is not None and key is not _DELETED:
            start, step = _probe_params(key, _size)
            idx = start
            while _keys[idx] is not None:
                idx = (idx + step) % _size
            _keys[idx] = key
            _values[idx] = old_values[i]
            _count += 1


def _find_slot(author: str) -> int:
    """Шукає індекс автора в хеш-таблиці; повертає -1, якщо автора не знайдено."""
    start, step = _probe_params(author, _size)
    idx = start

    for _ in range(_size):
        key = _keys[idx]
        if key is None:
            # Зустріли порожню комірку — автора точно немає в таблиці
            return -1
        if key is not _DELETED and key == author:
            return idx
        idx = (idx + step) % _size

    return -1


def _insert_sorted_unique(books: list[str], title: str) -> None:
    """Вставляє назву книги у відсортований список, якщо її там ще немає."""
    left = 0
    right = len(books)

    # Бінарний пошук позиції для вставки
    while left < right:
        mid = (left + right) // 2
        if books[mid] < title:
            left = mid + 1
        else:
            right = mid

    if left < len(books) and books[left] == title:
        # Книга вже є у списку — дублікати не додаємо
        return
    books.insert(left, title)


def _find_in_sorted(books: list[str], title: str) -> int:
    """Шукає індекс книги у відсортованому списку; повертає -1, якщо не знайдено."""
    left = 0
    right = len(books) - 1

    while left <= right:
        mid = (left + right) // 2
        if books[mid] == title:
            return mid
        elif books[mid] < title:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global _size, _count, _deleted_count, _keys, _values
    _size = 1009
    _count = 0
    _deleted_count = 0
    _keys = [None] * _size
    _values = [None] * _size


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global _count, _deleted_count

    # Якщо таблиця заповнена (разом із видаленими комірками) більш ніж на 60%,
    # виконуємо рехешування для збереження O(1) часу доступу
    if (_count + _deleted_count) * 10 >= _size * 6:
        new_size = _size * 2 if _count * 10 >= _size * 5 else _size
        _rehash(new_size)

    start, step = _probe_params(author, _size)
    idx = start
    first_deleted = -1

    for _ in range(_size):
        key = _keys[idx]
        if key is None:
            # Вставляємо нового автора в першу знайдену видалену або в поточну порожню комірку
            target = first_deleted if first_deleted != -1 else idx
            if first_deleted != -1:
                _deleted_count -= 1
            _keys[target] = author
            _values[target] = [title]
            _count += 1
            return
        if key is _DELETED:
            if first_deleted == -1:
                first_deleted = idx
        elif key == author:
            # Автор уже є в каталозі — додаємо книгу в його відсортований список
            _insert_sorted_unique(_values[idx], title)
            return
        idx = (idx + step) % _size


def find(author, title):
    """ Перевіряє чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    idx = _find_slot(author)
    if idx == -1:
        return False
    return _find_in_sorted(_values[idx], title) != -1


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global _count, _deleted_count

    idx = _find_slot(author)
    if idx == -1:
        return

    books = _values[idx]
    pos = _find_in_sorted(books, title)
    if pos == -1:
        return

    books.pop(pos)
    if not books:
        # Якщо в автора не залишилося книг, позначаємо комірку як видалену
        _keys[idx] = _DELETED
        _values[idx] = None
        _count -= 1
        _deleted_count += 1


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не містить книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    idx = _find_slot(author)
    if idx == -1:
        return []
    # Повертаємо копію списку, щоб зовнішній код не змінив внутрішні дані таблиці
    return list(_values[idx])
