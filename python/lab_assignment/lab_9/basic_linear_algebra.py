def vector_size_check(*vector_variables):
    result = len(set([len(i) for i in vector_variables])) == 1
    # set_of_vectors = set([])
    # for i in vector_variables:
    #     set_of_vectors.add(len(i))
    # if len(set_of_vectors) == 1:
    #     result = True
    # else:
    #     result = False
    return result


def vector_addition(*vector_variables):
    result = [sum(vector) for vector in zip(*vector_variables)]
    return result

    # result = []
    # for i in zip(*vector_variables):
    #     result.append(sum(i))
    # return result


def vector_subtraction(*vector_variables):
    if not vector_size_check(vector_variables):
        raise ArithmeticError
    result = [vector[0] - sum(vector[1:]) for vector in zip(*vector_variables)]
    result = []
    for vector in zip(*vector_variables):
        i = 0
        others = 0
        for j in vector:
            if not i:
                first = j
                i = 1
            else:
                others += j
        result.append(first - others)

    return result


def scalar_vector_product(alpha, vector_variable):
    result = [alpha * i for i in vector_variable]
    return result
    # result = []
    # for i in vector_variable:
    #     result.append(i * alpha)
    # return result


def matrix_size_check(*matrix_variables):
    column = set([len(set([len(column) for column in row]))for row in matrix_variables]) == {1}
    row = len(set([len(row) for row in matrix_variables])) == 1

    if column and row:
        result = True
    else:
        result = False
    return result

    # row = set()
    # column = set()
    # for i in matrix_variables:
    #     row.add(len(i))
    #     for j in i:
    #         column.add(len(j))
    # if len(row) == 1 and len(column) == 1:
    #     result = True
    # else:
    #     result = False
    # return result


def is_matrix_equal(*matrix_variables):
    # result = any([any([j[0] - j[1] for j in zip(*i)])for i in zip(*matrix_variables)]) == False
    # return result
    #
    elements = set()
    for i in zip(*matrix_variables):
        for j in zip(*i):
            elements.add(j[0] - j[1])

    if elements == {0}:
        result = True
    else:
        result = False
    return result


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    result = [[sum(j) for j in zip(*i)]for i in zip(*matrix_variables)]
    return result

    # result = []
    # result2 = []
    # for i in zip(*matrix_variables):
    #     for j in zip(*i):
    #         result.append(sum(j))
    #
    #     result2.append(result)
    #     result = []
    # return result2


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError

    result = [[j[0] - sum(j[1:]) for j in zip(*i)] for i in zip(*matrix_variables)]

    return result
    # matrix = []
    # for i in zip(*matrix_variables):
    #     vector = []
    #     for j in zip(*i):
    #         vector.append(j[0] - sum(j[1:]))
    #     matrix.append(vector)
    #
    #
    # return matrix


def matrix_transpose(matrix_variable):

    result = [list(i) for i in zip(*matrix_variable)]
    return result
    # result = []
    # for i in zip(*matrix_variable):
    #     result.append(list(i))
    # return result


def scalar_matrix_product(alpha, matrix_variable):

    result = [[scalar * alpha for scalar in vector] for vector in matrix_variable]
    return result

    # result = []
    # for vector in matrix_variable:
    #     new_vector = []
    #     for scalar in vector:
    #         new_vector.append(alpha * scalar)
    #     result.append(new_vector)
    # return result


def is_product_availability_matrix(matrix_a, matrix_b):

    result = set([len(row_a) - len(matrix_b) for row_a in matrix_a]) == {0}
    return result
    # first = set()
    # for row_a in matrix_a:
    #     first.add(len(row_a))
    # second = set([len(matrix_b)])
    #
    # if first == second:
    #     result = True
    # else:
    #     result = False
    # return result


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError

    result = [[sum(a*b for a,b in zip(column, row))for row in zip(*matrix_b)] for column in matrix_a]
    return result
    # result = []
    # for column in matrix_a:
    #     vector_list = []
    #     for row in zip(*matrix_b):
    #         vector = 0
    #         for a,b in zip(column, row):
    #             vector += (a*b)
    #         vector_list.append(vector)
    #     result.append(vector_list)
    #
    # return result

print(matrix_product([[1,2],[3,4]],[[5,6],[7,8]]))

if __name__ == "__main__":
    None