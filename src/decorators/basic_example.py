from functools import wraps

def interceptor(func):
    print("This is executed at function definition time (def my_func)")

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("This is executed before function call")
        result = func(*args, **kwargs)
        print("This is executed after function call")
        return result
    
    return wrapper

@interceptor
def my_func(n):
    print("This is my_func")
    print("n =", n)

my_func(4)