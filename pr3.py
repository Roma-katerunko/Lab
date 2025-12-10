students = {}  # тут зберігаємо ім'я і оцінку

while True:
    name = input("Введіть ім'я студента (або stop щоб завершити): ")

    if name.lower() == "stop":
        break

    grade = int(input("Введіть оцінку студента: "))
    students[name] = grade  # запис у словник

print("\nСписок студентів:")
for name, grade in students.items():
    print(name, "-", grade)   # вивід усіх студентів


average = sum(students.values()) / len(students)
# рахуємо середній бал

excellent = [name for name, g in students.items() if 10 <= g <= 12]
good = [name for name, g in students.items() if 7 <= g <= 9]
bad = [name for name, g in students.items() if 4 <= g <= 6]
failed = [name for name, g in students.items() if 1 <= g <= 3]
# категорії

print("\nСередній бал по групі:", average)
print("Відмінники (10-12):", len(excellent), excellent)
print("Хорошисти (7-9):", len(good), good)
print("Відстаючі (4-6):", len(bad), bad)
print("Не здали (1-3):", len(failed), failed)
