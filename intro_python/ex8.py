def even_odd():
    nb = int(input("Un nombre entier: \n"))
    if nb % 2 == 0:
        print("C'est pair")
    else:
        print("C'est impair")


def palindrome():
    mot = input("Un mot :\n")
    palindrome = mot[::-1]
    if mot.lower() == palindrome.lower():
        print(f"{mot} est un palindrome")
    else:
        print(f"{mot} n'est pas un palindrome")


if __name__ == '__main__':
    even_odd()
    palindrome()
