import sys


def student_key(student: tuple[str, str, str, str]) -> tuple[int, str, str]:
    """Ключ сортування: (номер класу, літера класу, прізвище)."""
    surname, _, grade, _ = student
    grade_num = int(grade[:-1])
    grade_letter = grade[-1]
    return (grade_num, grade_letter, surname)


def insertion_sort_students(students: list[tuple[str, str, str, str]]) -> None:
    """Сортує список особових справ методом вставки за класом, а потім за прізвищем."""
    for i in range(1, len(students)):
        current = students[i]
        current_key = student_key(current)
        j = i - 1
        while j >= 0 and student_key(students[j]) > current_key:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = current


def main() -> None:
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        return

    n = int(lines[0])
    students = []
    idx = 1
    for _ in range(n):
        surname = lines[idx]
        name = lines[idx + 1]
        grade = lines[idx + 2]
        birthdate = lines[idx + 3]
        students.append((surname, name, grade, birthdate))
        idx += 4

    # Сортуємо особові справи методом вставки
    insertion_sort_students(students)

    # Виводимо у форматі: <клас> <прізвище> <ім'я> <дата народження>
    out = [f"{grade} {surname} {name} {birthdate}" for surname, name, grade, birthdate in students]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
