import sys
sys.path.append("..")

from decorator.hide_output import hide_output

@hide_output
def demo():
    print("Це повідомлення НЕ видно")
    print("І це теж НЕ видно")

print("Початок")
demo()
print("Кінець")
