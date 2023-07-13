#!/usr/bin/python3
def calculate_sum(x, y):
    """Calculating the sum of two numbers."""
    result = x + y
    return result


def main():
    """Main function."""
    num1 = 10
    num2 = 20
    total = calculate_sum(num1, num2)
    print("The sum is:", total)


if __name__ == '__main__':
    main()
