def f(x):
    return x**2

def g(x):
    return x - 1

def compose_functions(f, g, x):
    return f(g(x))

x_value = 4

# ex (g ° f)(x)
result_g_of_f = compose_functions(f, g, x_value)
print("(g ° f)({}) = {}".format(x_value, result_g_of_f))

# exe (g ° g)(x)
result_g_of_g = compose_functions(g, g, x_value)
print("(g ° g)({}) = {}".format(x_value, result_g_of_g))

# ex (f ° f)(x)
result_f_of_f = compose_functions(f, f, x_value)
print("(f ° f)({}) = {}".format(x_value, result_f_of_f))

# ex (f ° g)(x)
result_f_of_g = compose_functions(f, g, x_value)
print("(f ° g)({}) = {}".format(x_value, result_f_of_g))
