import time
from collections import deque


def find_factorial():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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


def find_gcd():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while True:
        print("\n\nEnter first number or "
                "\npress <enter> to return to the Main Menu")

        ans = input("\n>>> ")
        if not ans:
            break
        num1 = int(ans)

        print("\n\nEnter second number or "
                "\npress <enter> to return to the Main Menu")

        ans = input("\n>>> ")
        if not ans:
            break
        num2 = int(ans)

        print(f"\n\nGCD of {num1} and {num2} is {gcd(num1, num2)}")


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def fibonacci():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while True:
        print("\n\nEnter number of fibonacci numbers to print or"
                "\npress <enter> to return to the Main Menu")

        ans = input("\n>>> ")
        if not ans:
            break
        n = int(ans)

        # join a list of strings created from a list of fibonacci terms
        fibs = ' '.join([str(num) for num in [fib(x) for x in range(0, n)]])

        print(f"\n\n{fibs}")


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def tower_of_hanoi():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while True:
        print("\n\nEnter number of disks or"
                "\npress <enter> to return to the Main Menu")

        ans = input("\n>>> ")
        if not ans:
            break
        n = int(ans)

        tower = Tower_Of_Hanoi(n)
        tower.execute()


class Tower_Of_Hanoi():
    def __init__(self, n):
        self.n = n
        self.source = deque(num for num in reversed(range(1, n + 1)))
        self.temp = deque()
        self.dest = deque()

    def display_pillars(self):
        pillars = ""
        for x in reversed(range(self.n)):
            pillars += (
                f"\n{self.source[x] if x < len(self.source) else ''}"
                f"\t{self.temp[x] if x < len(self.temp) else ''}"
                f"\t{self.dest[x] if x < len(self.dest) else ''}"
            )

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("A\tB\tC")
        print(pillars)
        print("-------------------")
        time.sleep(1)

    def execute(self):
        self.display_pillars()
        self.hanoi(self.n, self.source, self.temp, self.dest)

    def hanoi(self, n, source, temp, dest):
        if n == 1:
            disk = source.pop()
            dest.append(disk)
            self.display_pillars()
            return
        self.hanoi(n-1, source, dest, temp)
        dest.append(source.pop())
        self.display_pillars()
        self.hanoi(n-1, temp, source, dest)


options = [
    find_factorial,
    convert_base,
    find_gcd,
    fibonacci,
    tower_of_hanoi,
]

def main():
    quit = False
    while not quit:
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
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
