
def find_factorial():
    while True:
        print("\n\nEnter a number to find the factorial of or "
                "\npress <enter> to return to the Main Menu")

        ans = input("\n>>> ")
        if not ans:
            break

        num = int(ans)
        fact = factorial(num)

        print(f"\n{num}!: {fact}")

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

def convert_base():
    while True:
        print("\n\nEnter a number to convert or "
                "\npress <enter> to return to the Main Menu")

        ans = input("\n>>> ")
        if not ans:
            break
        num = int(ans)

        print(f"\n\nBinary Form: {converted(num, 2)}")
        print(f"Octal Form: {converted(num, 8)}")
        print(f"Hexadecimal Form: {converted(num, 16)}")


def converted(num, base):
    converted_list = []
    convert(num, base, converted_list)

    # list comprehension to create list of strings
    converted_str = [str(digit) for digit in converted_list]

    return ''.join(converted_str)


def convert(num, base, converted):
    if num == 0:
        return

    # integer division
    new_num = num // base
    convert(new_num, base, converted)
    rem = num % base
    if rem < 10:
        converted.append(rem)
    else:
        # convert number to letter if over 10
        converted.append(chr(rem - 10 + ord('A')))


def gcd():
    pass

def fibonacci():
    pass

def hanoi():
    pass


options = [
    find_factorial,
    convert_base,
    gcd,
    fibonacci,
    hanoi,
]

def main():
    quit = False
    while not quit:
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "Welcome to the Recursion app.\n"
            "\nPlease select one of the following options:\n"
            "1: Factorial\n"
            "2: Convert Base\n"
            "3: Greatest Common Divisor\n"
            "4: Fibonacci series\n"
            "5: Tower of Hanoi\n"
            "\n0: Quit\n"
        )
        choice = int(input("\n>>> "))
        print()

        if choice == 0:
            quit = True
        else:
            options[choice-1]()


if __name__ == "__main__":
    main()
