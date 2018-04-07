# -*- coding: utf-8 -*-


def is_positive_number(integer_str_value):

    try:
        int_value = int(integer_str_value)
        if int_value > 0:
            result = True
        else:
            result = False
    except:
        result = False

    return result


def get_factorial_value(integer_value):
    #
# '''
# Input:
#   -  integer_value : 자연수 값
# Output:
#   -  integer_value의 Factorial 값
# Examples:
#    >>> import factorial_calculator as fc
#    >>> fc.get_factorial_value(5)
#    120
#    >>> fc.get_factorial_value(7)
#    5040
# '''
# ===Modify codes below=============
    result = 1
    for i in range(1, integer_value + 1):
        result *= i

    return result

print(get_factorial_value(5))
# ==================================


def main():
    user_input = 999


if __name__ == "__main__":
    main()
