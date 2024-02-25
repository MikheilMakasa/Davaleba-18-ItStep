class PositiveFunctor:
    def __init__(self, func):
        self.func = func

    def __call__(self, num):
        if num < 0:
            raise ValueError("Number must be positive.")
        result = self.func(num)
        print(f"Result: {result}")
        return result

@PositiveFunctor
def return_number(num):
    return num


try:
    return_number(10)
    return_number(-2) 
except ValueError as e:
    print(f"Error: {e}")
