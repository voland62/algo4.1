import re
import sys


class VocabularyHashTable:
    """Хеш-таблиця з відкритою адресацією для слів словника та відміток їх використання."""

    def __init__(self, capacity: int = 4099) -> None:
        # Простий розмір 4099 при N <= 1000 гарантує коефіцієнт заповнення < 0.25
        self._size = capacity
        self._keys = [None] * capacity
        self._used = [False] * capacity
        self._vocab_count = 0
        self._used_count = 0

    def _hash(self, word: str) -> int:
        """Власна поліноміальна хеш-функція для рядка (без вбудованої hash())."""
        h = 0
        for ch in word:
            h = (h * 31 + ord(ch)) & 0x7FFFFFFF
        return h % self._size

    def add_word(self, word: str) -> None:
        """Додає слово зі словника до хеш-таблиці."""
        idx = self._hash(word)
        while self._keys[idx] is not None:
            if self._keys[idx] == word:
                # Слово вже додано до словника
                return
            idx = (idx + 1) % self._size

        self._keys[idx] = word
        self._vocab_count += 1

    def mark_used(self, word: str) -> bool:
        """Позначає слово як використане; повертає False, якщо слова немає у словнику."""
        idx = self._hash(word)
        while self._keys[idx] is not None:
            if self._keys[idx] == word:
                if not self._used[idx]:
                    self._used[idx] = True
                    self._used_count += 1
                return True
            idx = (idx + 1) % self._size

        # Слово відсутнє в словнику
        return False

    def all_used(self) -> bool:
        """Перевіряє, чи всі слова словника були використані хоча б один раз."""
        return self._used_count == self._vocab_count


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # Зчитуємо кількість слів у словнику N та кількість рядків тексту M
    first_parts = lines[0].split()
    n = int(first_parts[0])
    m = int(first_parts[1])

    # Заповнюємо хеш-таблицю словами зі словника (у нижньому регістрі)
    vocab = VocabularyHashTable()
    for i in range(1, n + 1):
        word = lines[i].strip().lower()
        if word:
            vocab.add_word(word)

    # Об'єднуємо M рядків тексту твору та виділяємо всі слова з латинських літер
    essay_text = "\n".join(lines[n + 1 : n + 1 + m])
    words = re.findall(r"[a-zA-Z]+", essay_text)

    # Перевіряємо кожне слово твору на наявність у словнику
    for w in words:
        if not vocab.mark_used(w.lower()):
            sys.stdout.write("Some words from the text are unknown.\n")
            return

    # Перевіряємо, чи використано весь словник
    if vocab.all_used():
        sys.stdout.write("Everything is going to be OK.\n")
    else:
        sys.stdout.write("The usage of the vocabulary is not perfect.\n")


if __name__ == "__main__":
    main()
