a = "I am global variable!"


def enclosing_funcion_1():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)
    return inner_function


def enclosing_funcion_2_1():
    a = "I am variable from enclosed function!"

    def inner_function():

        global a
        print(a)
    return inner_function


def enclosing_funcion_2_2():
    a = "I am variable from enclosed function!"

    def inner_function():

        nonlocal a
        print(a)
    return inner_function
