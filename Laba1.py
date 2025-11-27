cile_chyslo = 10               # int
drobove_chyslo = 3.14          # float
ryadok = "Привіт, світ!"       # str
pravda_chy_brehnya = True       # bool
spisok = [1, 2, 3, 4, 5]      # list
kortegh = (10, 20, 30)         # tuple
mnoghina = {1, 2, 3, 4}        # set
slovnik: dict[str, str | int] = {"name": "Max", "age": 16}  # dict

print(f"ціле_число, {type(cile_chyslo)} : {cile_chyslo}")
print(f"дробове_число, {type(drobove_chyslo)} : {drobove_chyslo}")
print(f"рядок, {type(ryadok)} : {ryadok}")
print(f"логічне_значення, {type(pravda_chy_brehnya)} : {pravda_chy_brehnya}")
print(f"список, {type(spisok)} : {spisok}")
print(f"кортеж, {type(kortegh)} : {kortegh}")
print(f"множина, {type(mnoghina)} : {mnoghina}")
print(f"словник, {type(slovnik)} : {slovnik}")


a = 7 # присвоєння
b = 3

print("a + b =", a + b)   # додавання
print("a - b =", a - b)   # віднімання
print("a * b =", a * b)   # множення
print("a / b =", a / b)   # ділення
print("a // b =", a // b) # цілочисельне ділення
print("a % b =", a % b)   # остача від ділення
print("a ** b =", a ** b) # піднесення до степеня