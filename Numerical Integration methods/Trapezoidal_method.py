import math
from colors import bcolors


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return integral
2

if __name__ == '__main__':
<<<<<<< HEAD
    f = lambda x:()
    result = trapezoidal_rule(f, 3, 4, 10)
    print(bcolors.OKBLUE,"Approximate integral:", result, bcolors.ENDC)
=======
    f = lambda x: math.tan(x)
    result = trapezoidal_rule(f, 1, 3, 200)
    print(bcolors.OKBLUE, "Approximate integral:", result, bcolors.ENDC)
>>>>>>> origin/main
