# -*- coding: utf-8 -*-

from function import f


def biseccion(a, b, tolerance, max_iterators):
    return_list = []

    a_evaluated_f = float(f(a))
    b_evaluated_f = float(f(b))

    if a_evaluated_f == 0:

        print("root on" + str(a))

    elif b_evaluated_f == 0:

        print("root on" + str(b))

    elif a_evaluated_f * b_evaluated_f < 0:

        count = 1

        x_middle = float((a + b) / 2)
        y_middle = float(f(x_middle))

        error = tolerance + 1

        return_list.append([count, a, b, x_middle, y_middle, 0])

        while error > tolerance and y_middle != 0 and count < max_iterators:

            if a_evaluated_f * y_middle < 0:

                b = x_middle
                b_evaluated_f = y_middle

            else:

                a = x_middle
                a_evaluated_f = y_middle

            aux_middle = x_middle

            x_middle = (a + b) / 2
            y_middle = f(x_middle)

            error = abs(x_middle - aux_middle)

            count += 1

            return_list.append([count, a, b, x_middle, y_middle, error])

    return return_list


def main():
    print("ingrese a")
    a = input()
    print("ingrese b")
    b = input()
    print("ingrese tolerancia")
    tolerancia = input()
    print(tolerancia)
    print("ingrese repeticiones")
    repeticiones = input()

    tabla = biseccion(a, b, tolerancia, repeticiones)


    i=0
    while i < len(tabla):
        print(" | "+str(tabla[i][0])+" | "+str(tabla[i][1])+" | "+str(tabla[i][2])+" | "+str(tabla[i][3])+" | "+str(tabla[i][4])+" | "+str(tabla[i][5])+" | ")
        i += 1


if __name__ == "__main__":
    main()

