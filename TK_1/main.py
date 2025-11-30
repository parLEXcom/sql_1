import os
from colorama import Fore, Style

# print(os.path.basename("/Users/lex/PycharmProjects/PythonProject/TK_1"))


# class Drf:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def fgh(self):
#         print(self.x + self.y)
#
#     def qrt(self):
#         print(f"Икс равен {self.x}")
#
#
# qwe = Drf(2, 4)

# qwe.fgh()
# qwe.qrt()
#
# qwe(5, 6)
a = ["1", "2", "3", "4", "5"]


b = "--".join(a)


print(b)
# for i in a:
#     print(i)

""" 
Рисование линий


print("_" * 16)
print("|", " " *12, "|")
print("|", " " *12, "|")
print("_" * 16)
"""

def draw_colored_square(size, color):
    for i in range(size):
        for j in range(size):
            print(color + '=' + Style.RESET_ALL, end=' ')
        print()

# Пример использования
draw_colored_square(2, Fore.RED)
