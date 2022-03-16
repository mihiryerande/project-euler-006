# Problem 006:
#     Sum Square Difference
#
# Description:
#     The sum of the squares of the first ten natural numbers is:
#         1^2 + 2^2 + ... + 10^2 = 385
#     The square of the sum of the first ten natural numbers is:
#         (1 + 2 + ... + 10)^2 = 3025
#
#     Hence the difference between the sum of the squares of the first ten natural numbers
#       and the square of the sum is:
#         3025 - 385 = 2640
#
#     Find the difference between the sum of the squares of the first one hundred natural numbers
#       and the square of the sum.

def main(n):
    """
    Return the difference between...
      the sum of the squares of the first `n` natural numbers and
      the square of their sum.

    Args:
        n (int): Natural number

    Returns:
        Difference between sum of squares and square of sum.

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0

    # Sum of squares equals:
    #   n * (n+1) * (2n+1) / 6
    # Sum of all equals:
    #   n * (n+1) / 2
    # Square of ^that^ sum:
    #   ( n * (n+1) / 2 )^2
    #   = n^2 * (n+1)^2 / 4
    #
    # Difference simplifies down to:
    #   (n-1) * n * (n+1) * (3n+2) / 12
    return (n-1) * n * (n+1) * (3*n+2) // 12


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    diff = main(num)
    print('Difference between `square of sum` and `sum of squares` for {}:\n{}'.format(num, diff))
