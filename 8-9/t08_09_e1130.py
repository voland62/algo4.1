import sys


def build_ways(max_len: int, max_sum: int) -> list[list[int]]:
    """Обчислює ways[l][s] — кількість послідовностей із l цифр (0..9) із сумою s."""
    ways = [[0] * (max_sum + 1) for _ in range(max_len + 1)]
    ways[0][0] = 1
    for length in range(1, max_len + 1):
        for s in range(max_sum + 1):
            total = 0
            for d in range(10):
                if s >= d:
                    total += ways[length - 1][s - d]
            ways[length][s] = total
    return ways


def count_bounded(suffix_limit: str, target_sum: int, ways: list[list[int]]) -> int:
    """Рахує кількість рядків цифр довжини len(suffix_limit), <= suffix_limit із сумою target_sum."""
    rem_len = len(suffix_limit)
    if target_sum < 0 or target_sum > 9 * rem_len:
        return 0

    total = 0
    cur_sum = target_sum
    for i, ch in enumerate(suffix_limit):
        limit_d = int(ch)
        rest = rem_len - 1 - i
        # Цифри, строго менші за поточну цифру межі — далі обмежень немає
        for d in range(limit_d):
            if cur_sum >= d:
                total += ways[rest][cur_sum - d]
        cur_sum -= limit_d
        if cur_sum < 0:
            return total

    # Якщо саме число suffix_limit має рівно потрібну суму цифр
    if cur_sum == 0:
        total += 1
    return total


def count_with_prefix(prefix: str, target_sum: int, n_str: str, ways: list[list[int]]) -> int:
    """Рахує кількість чисел у [1, n] із сумою цифр target_sum, запис яких починається з prefix."""
    p_len = len(prefix)
    n_len = len(n_str)
    pref_sum = sum(int(ch) for ch in prefix)
    rem_sum = target_sum - pref_sum

    if rem_sum < 0 or p_len > n_len:
        return 0

    total = 0
    # Довжини строго менші за довжину n: обмежень на цифри немає
    for length in range(p_len, n_len):
        rem_len = length - p_len
        if rem_sum <= 9 * rem_len:
            total += ways[rem_len][rem_sum]

    # Довжина дорівнює довжині n: порівнюємо префікс із префіксом n
    n_pref = n_str[:p_len]
    rem_len = n_len - p_len
    if prefix < n_pref:
        if rem_sum <= 9 * rem_len:
            total += ways[rem_len][rem_sum]
    elif prefix == n_pref:
        total += count_bounded(n_str[p_len:], rem_sum, ways)

    return total


def find_position(n: int, k: int, ways: list[list[int]]) -> int:
    """Знаходить 1-індексовану позицію числа k у градуйованому лексикографічному порядку [1..n]."""
    n_str = str(n)
    k_str = str(k)
    w = sum(int(ch) for ch in k_str)

    pos = 1
    # Додаємо всі числа з меншою сумою цифр
    for s in range(1, w):
        for d in range(1, 10):
            pos += count_with_prefix(str(d), s, n_str, ways)

    # Додаємо числа з такою ж сумою цифр w, які лексикографічно менші за k_str
    pref = ""
    pref_sum = 0
    for i, ch in enumerate(k_str):
        # Якщо власний непорожній префікс має суму цифр w, він стоїть перед k_str
        if i > 0 and pref_sum == w:
            pos += 1
        cur_d = int(ch)
        start_d = 1 if i == 0 else 0
        for d in range(start_d, cur_d):
            pos += count_with_prefix(pref + str(d), w, n_str, ways)
        pref += ch
        pref_sum += cur_d

    return pos


def find_kth_number(n: int, k: int, ways: list[list[int]]) -> int:
    """Знаходить число, яке стоїть на k-ій позиції у градуйованому лексикографічному порядку [1..n]."""
    n_str = str(n)
    max_w = 9 * len(n_str)

    # Знаходимо суму цифр w шуканого числа
    w = 1
    while w <= max_w:
        cnt = 0
        for d in range(1, 10):
            cnt += count_with_prefix(str(d), w, n_str, ways)
        if k <= cnt:
            break
        k -= cnt
        w += 1

    # Відновлюємо число цифра за цифрою в лексикографічному порядку
    pref = ""
    pref_sum = 0
    while True:
        if pref and pref_sum == w:
            if k == 1:
                return int(pref)
            k -= 1

        start_d = 1 if not pref else 0
        for d in range(start_d, 10):
            cnt = count_with_prefix(pref + str(d), w, n_str, ways)
            if k <= cnt:
                pref += str(d)
                pref_sum += d
                break
            k -= cnt


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    k = int(data[1])

    max_len = len(str(n))
    ways = build_ways(max_len, 9 * max_len)

    pos_of_k = find_position(n, k, ways)
    num_at_k = find_kth_number(n, k, ways)

    sys.stdout.write(f"{pos_of_k}\n{num_at_k}\n")


if __name__ == "__main__":
    main()
