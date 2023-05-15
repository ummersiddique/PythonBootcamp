# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def print_hi(name):
    fib(30)
    # Use a breakpoint in the code line below to debug your script.
    a = 12
    dummy = "Youtube"
    print("Char " + dummy[6])
    string = "Hi there"
    print(string)
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(a)


def number():
    print("Getting number")
    return 5


def number_for_sum():
    print("Getting number for sum")
    return 10


def operators():
    print(f'Sum is {5 + 5}')
    print(f'Difference {5 - 5}')
    print(f'Product : {5 * 5}')
    print(f'Quotient : {5 / 5}')
    print(f'Integer Quotient : {5 // 5}')
    print(f'Remainder : { 5 % 2}')
    print(f'5 ** 5 : {5 ** 5}')
    print(f'Order : {5 + 5 * 5}')
    print(f'Order : {number_for_sum() + 10 - number()}')
    print("--------------------------------------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    operators()
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
