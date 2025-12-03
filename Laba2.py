lst = [5, 2, 14, 7, 8, 22, 1, 4, 19, 9,
       "apple", "banana", "pear", "kiwi", "plum",
       "grape", "mango", "lime", "cherry", "orange"]
# створюємо список з 10 чисел і 10 строк

ints = []
strings = []
# окремі списки для int і str

for x in lst:
    if type(x) == int:
        ints.append(x)  # додаємо число
    else:
        strings.append(x)  # додаємо строку
# розділяємо елементи по типу

ints.sort()
strings.sort()
# сортуємо кожну групу

sorted_list = ints + strings
# об’єднуємо: спочатку числа, потім строки

even_list = [x for x in ints if x % 2 == 0]  # список парних чисел

caps_list = [s.upper() for s in strings]
# строки капсом

print("Основний список:", lst)
print("Відсортований:", sorted_list)
print("Парні:", even_list)
print("Строки капсом:", caps_list)
# вивід результатів