

def determinant_2x2(matrix):

    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def determinant_nxn(matrix):

    if len(matrix) == 2:
        return determinant_2x2(matrix)
    det = 0
    for i in range(len(matrix)):
        minor = [row[:i] + row[i + 1:] for row in matrix[1:]]
        det += (-1) ** i * matrix[0][i] * determinant_nxn(minor)
    return det


def cramer_solve_2x2(A, b):

    det_A = determinant_2x2(A)
    if det_A == 0:
        raise ValueError("Матрица вырождена, решение не существует.")

    A1 = [[b[0], A[0][1]],
          [b[1], A[1][1]]]
    A2 = [[A[0][0], b[0]],
          [A[1][0], b[1]]]

    det_A1 = determinant_2x2(A1)
    det_A2 = determinant_2x2(A2)

    x1 = det_A1 / det_A
    x2 = det_A2 / det_A

    return x1, x2


def cramer_solve_nxn(A, b):
    det_A = determinant_nxn(A)
    if det_A == 0:
        raise ValueError("Матрица вырождена, решение не существует.")

    n = len(A)
    x = [0] * n

    for i in range(n):
        A_i = [row[:] for row in A]
        for j in range(n):
            A_i[j][i] = b[j]
        det_A_i = determinant_nxn(A_i)
        x[i] = det_A_i / det_A

    return x


def cramer_solve_nxn_complex(A, b):
    det_A = determinant_nxn(A)
    if det_A == 0:
        raise ValueError("Матрица вырождена, решение не существует.")

    n = len(A)
    x = [0] * n

    for i in range(n):
        A_i = [row[:] for row in A]
        for j in range(n):
            A_i[j][i] = b[j]
        det_A_i = determinant_nxn(A_i)
        x[i] = det_A_i / det_A

    return x


def input_matrix(size):
    """
    Ввод матрицы коэффициентов.

    :param size: размер матрицы (nxn)
    :return: матрица коэффициентов
    """
    A = []
    for i in range(size):
        row = []
        for j in range(size):
            val = input(f"Элемент A[{i + 1}][{j + 1}]: ")
            row.append(complex(val))
        A.append(row)
    return A


def input_vector(size):
    """
    Ввод вектора свободных членов.

    :param size: размер вектора
    :return: вектор свободных членов
    """
    b = []
    for i in range(size):
        val = input(f"Элемент b[{i + 1}]: ")
        b.append(complex(val))
    return b


def main():
    print("Выберите метод решения СЛАУ:")
    print("1. Метод Крамера для матриц 2x2")
    print("2. Метод Крамера для матриц nxn")
    print("3. Метод Крамера для матриц nxn с комплексными коэффициентами")
    choice = int(input("Введите номер метода: "))

    if choice == 1:
        A = [[complex(input("A[1][1]: ")), complex(input("A[1][2]: "))],
             [complex(input("A[2][1]: ")), complex(input("A[2][2]: "))]]
        b = [complex(input("b[1]: ")), complex(input("b[2]: "))]
        x1, x2 = cramer_solve_2x2(A, b)
        print(f"Решение системы: x1 = {x1}, x2 = {x2}")
    elif choice == 2:
        size = int(input("Введите размер матрицы nxn: "))
        A = input_matrix(size)
        b = input_vector(size)
        x = cramer_solve_nxn(A, b)
        print(f"Решение системы: x = {x}")
    elif choice == 3:
        size = int(input("Введите размер матрицы nxn: "))
        A = input_matrix(size)
        b = input_vector(size)
        x = cramer_solve_nxn_complex(A, b)
        print(f"Решение системы: x = {x}")
    else:
        print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

"""
Пример работы!
№1
Ввод 
2
1
1
3
5 
7
Ответ x1 = (1.6+0j), x2 = (1.8+0j) ВЕРНО
№2
Ввод
    [2, 1, 1],
    [1, 3, 1],
    [1, 1, 4]])
b = [5, 7, 9]
Ответ: x = [(0.9411764705882353+0j), (1.4705882352941178+0j), (1.6470588235294117+0j)] ВЕРНО

№3
            [2+1j, 1-2j, 1],
            [1-2j, 3+1j, 1],
            [1, 1, 4]
b = [5+2j, 7-1j, 9]
Ответ  x = [(1.5416427340608847+0.9569213095921884j), (0.6990235496840895+0.24238943136128663j), (1.6898334290637564-0.2998276852383687j)]
"""

