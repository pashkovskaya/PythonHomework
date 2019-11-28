def remember_result(function):
    last_result = None

    def decorator(*args):
        nonlocal last_result
        print(f"Last result = '{last_result}'")
        args = map(str, args)
        last_result = function(*args)
    return decorator


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


sum_list("ac", "dc")
sum_list("lol", "kek")
sum_list("1", "2", "3")
