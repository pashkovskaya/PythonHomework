def call_once(func_to_call_once):
    called = False

    def decorator(*args):
        nonlocal called
        if not called:
            called = True
            return func_to_call_once(*args)
    return decorator


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(9, 2))
print(sum_of_numbers(1, 5))
print(sum_of_numbers(1, 9))
