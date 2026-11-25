import sys


def binary_search(collection: list[int], target: int) -> bool:
    """Виконує бінарний пошук елемента target у відсортованому списку collection."""
    left = 0
    right = len(collection) - 1

    while left <= right:
        # Знаходимо індекс середнього елемента поточного відрізка
        mid = (left + right) // 2

        if collection[mid] == target:
            # Елемент знайдено в колекції
            return True
        elif collection[mid] < target:
            # Шуканий елемент більший за середній — відкидаємо ліву половину
            left = mid + 1
        else:
            # Шуканий елемент менший за середній — відкидаємо праву половину
            right = mid - 1

    # Елемент відсутній у колекції
    return False


def main() -> None:
    # Зчитуємо всі вхідні дані за один раз для швидкої роботи при великих n та m
    data = sys.stdin.read().split()
    if not data:
        return

    # Зчитуємо кількість видів метеликів у колекції та самі номери (вже відсортовані)
    n = int(data[0])
    collection = [int(x) for x in data[1 : n + 1]]

    # Зчитуємо кількість запитів та номери метеликів для перевірки
    m = int(data[n + 1])
    queries = [int(x) for x in data[n + 2 : n + 2 + m]]

    # Для кожного запиту перевіряємо наявність у колекції за допомогою бінарного пошуку
    results = ["YES" if binary_search(collection, k) else "NO" for k in queries]

    # Виводимо всі відповіді по одній у рядку
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
