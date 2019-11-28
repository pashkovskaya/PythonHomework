def generate_squares(num: int) -> dict:
    return {i : i**2 for i in range(1, num + 1)}


print(generate_squares(5))
