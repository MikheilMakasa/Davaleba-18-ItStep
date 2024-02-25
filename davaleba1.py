
def positive_decorator(func):
    def wrapper(num):
        if num < 0:
            raise ValueError("Number must be positive.")
        result = func(num)
        print(f"Result: {result}")
        return result
    return wrapper

@positive_decorator
def return_number(num):
    return num


try:
    return_number(10)
    return_number(-2)  
except ValueError as e:
    print(f"Error: {e}")
