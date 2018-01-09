def vector_size_check(vector_variables):

    first_vector,*second_vector = vector_variables
    is_it_true = False
    for t in second_vector:
        while is_it_true == False:
            if len(first_vector) == len(t):
                print('a')
                is_it_true= True
            else:
                is_it_true = False
            if is_it_true == False: break

    return is_it_true


def vector_addition(*vector_variables):
    return None


def vector_subtraction(*vector_variables):
    if not vector_size_check(vector_variables):
        raise ArithmeticError
    return None


def scalar_vector_product(alpha, vector_variable):
    return None


def matrix_size_check(*matrix_variables):
    return None


def is_matrix_equal(*matrix_variables):
    return None


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return None


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return None


def matrix_transpose(matrix_variable):
    return None


def scalar_matrix_product(alpha, matrix_variable):
    return None


def is_product_availability_matrix(matrix_a, matrix_b):
    return None


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return None


if __name__ == "__main__":
    print(vector_size_check([[1, 2], [3, 4], [5, 6, 9]]))