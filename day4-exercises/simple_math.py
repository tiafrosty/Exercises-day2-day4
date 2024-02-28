"""
 Contains a collection of simple math commands.
""" 

def simple_add(a,b):
    
    """
    Return the first Fibonacci number above n.
    Iteratively calculate Fibonacci numbers until it finds one
    greater than n, which it then returns.

    Parameters
    ----------
    a : integer
        The minimum threshold for the desired Fibonacci number.
    b : integer
        The first Fibonacci number greater than the input, `n`.

    Returns
    -------
    
    Examples
    --------
    >>> fib.fib(1)
    2
    >>> fib.fib(3)
    5
    """

    return a+b

def simple_sub(a,b):
    """ A simple subtraction function. Performs subtraction of the two numbers

    Parameters
    ----------
    a : float
        The numebr to subtract from
    b : float
    The subtracted number

    Returns
    -------
    The difference of the given numbers
    
    Examples
    --------
    >>> simple_math.simple_sub(10, 5)
    5 """
    return a-b

def simple_mult(a,b):
    
    """ A simple multiplication function. Performs multiplication of the two numbers
    Parameters
    ----------
    a : float
    The first number in the product
    b : float
    The second number in the product

    Returns
    -------
    The prodcut of the given values
    
    Examples
    --------
    >>> simple_math.simple_mult(1, 4)
    4 """
    return a*b

def simple_div(a,b):

    """ A simple divide function. Performs division of the two numbers

    Parameters
    ----------
    a : float
    The numerator
    b : float
    The denominator

    Returns
    -------
    The fraction of the given values

    Examples
    --------
    >>> simple_math.simple_div(1, 4)
    0.25 """

    return a/b

def poly_first(x, a0, a1):

    """ A simple polynomial function. Returns the polynomial of the given numbers

    Parameters
    ----------
    x : float
        A first number in the sum
    a0 : float
        A second number in the sum
    a1 : float
        A second number in the sum

    Returns
    -------
    The polynomial a0 + a1*x of the given numbers

    Examples
    --------
    >>> simple_math.poly_first(1, 4)
    5 """

    return a0 + a1*x

def poly_second(x, a0, a1, a2):

    """ A not so simple second order polynomial function. Returns the polynomial of the given numbers

    Parameters
    ----------
    x : float
        A first number in the sum
    a0 : float
        A second number in the sum
    a1 : float
    A second number in the sum

    Returns
    -------
    A second order polynomial of the given numbers 

    Examples
    --------
    >>> simple_math.poly_first(1, 4)
    5 """

    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
