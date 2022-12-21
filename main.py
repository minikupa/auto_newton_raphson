import sympy
from sympy import degree

x = sympy.symbols("x")
init_fx = x ** 20 + 3 * x ** 7 - 8


def solve(fx, f_prime, init_x):
    x_temp = init_x - 0.1
    x_later = init_x

    while abs(x_later - x_temp) > 0.000001:
        x_temp = x_later
        y = fx.subs(x, x_later)
        y_prime = float(f_prime.subs(x, x_later))

        x_later = x_later - y / y_prime
    return x_later


def calculate(fx):
    f_prime = sympy.diff(fx, x)

    order = degree(fx, x)
    if order != 1:
        root = calculate(f_prime)

        list = []
        print(str(order) + " >>>> " + str(fx))
        for index, value in enumerate(root):
            if index + 1 != len(root):
                average_x = (root[index] + root[index + 1]) / 2
                if f_prime.subs(x, average_x) == 0:
                    if fx.subs(x, average_x) == 0:
                        list.append(average_x)
                else:
                    if f_prime.subs(x, 0) != 0:
                        list.append(solve(fx, f_prime, average_x))

            else:
                list.append(solve(fx, f_prime, root[0] - 1))
                list.append(solve(fx, f_prime, root[len(root) - 1] + 1))

        round_list = [round(value, 4) for value in list]
        list.sort()

        print(str(order) + " >>>> " + str(set(round_list)))
        return list

    else:
        return [solve(fx, f_prime, 0)]


calculate(init_fx)
