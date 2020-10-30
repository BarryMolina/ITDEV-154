
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
    pass

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
