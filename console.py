!/usr/bin/python3
def calculate_sum(a, b):
    """
    This function calculates the sum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")

    return a + b


def main():
    """
    The main function that calls the calculate_sum function.
    """
    result = calculate_sum(5, 3)
    print(f"The sum of 5 and 3 is {result}.")


if __name__ == "__main__":
    main()


