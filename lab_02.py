# coding=windows-1251
import numpy as np
import unittest
from sympy import symbols, integrate

def f_upper(x):
    return 2 * x**2 + 1

def f_lower(x):
    return -2 * x**2 + 7

def simpson_method(f1, f2, a, b, n):
    if n % 2 == 1:
        n += 1  
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    fx = f1(x) - f2(x)
    integral = (h / 3) * (fx[0] + 4 * sum(fx[1:-1:2]) + 2 * sum(fx[2:-2:2]) + fx[-1])
    return integral

def exact_integral():
    x = symbols('x')
    integral_expr = (2*x**2 + 1) - (-2*x**2 + 7)
    result = integrate(integral_expr, (x, 5, 6))
    return float(result)

class test_simpson_method(unittest.TestCase):
    def test_simpson_accuracy(self):
        exact_value = exact_integral()
        for steps in [2, 10, 20, 50]: 
            approx_value = simpson_method(f_upper, f_lower, 5, 6, steps)
            self.assertAlmostEqual(approx_value, exact_value, places=10)
            print(f"кол-во разбиений={steps}: Симпсон={approx_value}, Точное={exact_value}") 

if __name__ == '__main__':
    unittest.main()
