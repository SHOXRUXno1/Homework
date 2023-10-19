def Foydalanuvchi():
    """Kvadrat va kubni konsolga chiqaruvchi funksiya"""
    print(Foydalanuvchi.__doc__)
    square = int(input("Hohlagan natural son yozing>>"))
    print(f"{square} ning kavadrati, = {square ** 2} ga teng")
    print(f"{square} ning kubi, = {square ** 3} ga teng")


Foydalanuvchi()


def Foydalanuvchi1():
    """Juft yoki Toqligini tekshiruvchi funksiya"""
    print(Foydalanuvchi1.__doc__)
    number = int(input("Hohlagan natural son yozing>>"))
    if (number % 2) == 0:
        print(f"{number} Juft son")
    else:
        print(f"{number} Toq son")


Foydalanuvchi1()
