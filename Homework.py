def Foydalanuvchi(x):
    """Kvadrat va kubni konsolga chiqaruvchi funksiya"""
    print(Foydalanuvchi.__doc__)
    print(f"{x} ning kvadrati = {x ** 2} ga tneg")
    print(f"{x} ning kubi = {x ** 3} ga teng ")


Foydalanuvchi(5)


def Foydalanuvchi1(y):
    """Juft yoki Toqligini tekshiruvchi funksiya"""
    print(Foydalanuvchi1.__doc__)
    if (y % 2) == 0:
        print(f"{y} Juft son")
    else:
        print(f"{y} Toq son")


Foydalanuvchi1(3)
