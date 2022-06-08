#adar katzir  209502293
import math
import numpy as np

def secant_method(x0, x1, tol):
    x2 = 0
    min_section = x0
    max_section = x1
    iter = 1
    condition = True
    x1s = []
    x0s = []
    fx0s = []

    while condition:
        if f(x0) == f(x1):
            print("Divide by zero error!")
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        if x2 > max_section or x2 < min_section:
            x2 = None
            break
        x0s.append(x0)
        x1s.append(x1)
        fx0s.append(f(x0))
        x0 = x1
        x1 = x2
        iter += 1

        condition = abs(f(x2)) > tol
    if x2 is not None:
        for x0 in range(len(x0s)):
            print(f"iteration = {x0 + 1} x0 = {x0s[x0]}, x1 = {x1s[x0]}, f(x0) = {fx0s[x0]}")

        print("**************************************************************************")
        print(f"Section [{min_section:.2f} ,{max_section:.2f}]: Found solution after {iter} iterations: {x2}")
        print("**************************************************************************")


def f(x):
    return math.sin(2*math.e**(-2*x))/(2*x**3+5*x**2-6)

if __name__ == "__main__":
    epsilon = 1e-6
    min_range = -1
    max_range = 1.2
    step = 0.5
    secant_section_list = []

    for i in np.arange(min_range, max_range, step):
        i = round(i, 2)
        if f(i) * f(i + 0.1) <= 0:
            secant_section_list.append((i, i + step))

    print("---------------------------------------------------------------------------------------------")
    print("Roots by secant method for f(x) = math.sin(2*math.e**(-2*x))/(2*x**3+5*x**2-6):")
    print("--------------------------------------------------------------------------------------------")

    if len(secant_section_list) == 0:
        print("No roots were found using a secant method")
    else:
        for section in secant_section_list:
            secant_method(section[0], section[1], epsilon)
