# my file of calculus in one variable
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def n_derivatives(expr, n=1):
    """Function that returns a list with the n derivatives of an expression, with n given.

    Args: 
        expr: Any sympy function
        n (int, optional): The number of derivatives required. Defaults to one.

    Returns:
        list: the funtion and the indicated derivatives.

    Example:
        >>> from sympy import symbols
        >>> x = symbols('x')
        >>> n_derivatives(x**4, 4)
        [x**4, 4*x**3, 12*x**2, 24*x, 24]"""
    derivatives = [expr]
    x = sp.symbols('x')
    for i in range(n):
        derivatives.append(sp.Derivative(derivatives[-1], x).doit())
    return derivatives


def graph_fyd(expression):
    """Function that graphs an expression given as a string and its derivative in the same plane.

    Args: 
        expression (str) : Expression of a function.

    Example:
        >>> import matplotlib.pyplot as plt
        >>> graph_fyd("x**2")
        .. image:: graph_fyd.png
            :align: center"""
    x = sp.symbols('x')
    expr = sp.sympify(expression)
    deriv = sp.diff(expr, x)
    f, f_prime = sp.lambdify(x, expr, 'numpy'), sp.lambdify(x, deriv, 'numpy')
    domain = np.linspace(-10, 10)
    f_eval = f(domain)
    f_prime_eval = f_prime(domain)
    if type(f_prime_eval) == float or type(f_prime_eval) == int:
        for j in range(len(domain) - 1):
            f_prime_eval = np.append(f_prime_eval, [f_prime(domain)])

    fig, ax = plt.subplots()
    ax.set_title("Function and derivative")
    ax.plot(domain, f_eval, label=expression)
    ax.plot(domain, f_prime_eval, label="Derivative")
    ax.set_xlabel("$x$")
    ax.legend(loc='center',
              bbox_to_anchor=(0.78, -0.13),
              shadow=True,
              ncol=2)
    plt.draw_if_interactive()
