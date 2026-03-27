import time


# start = time.time()
# print("hello")
# end = time.time()
# print(end - start)
def measureTime(unit="sec"):
    def decorator(function):
        def wrapper(*args, **kwargs):
            start = time.time()
            function(*args, **kwargs)
            end = time.time()
            res = end - start
            if unit == "msec":
                res = res * 1000
            print(f"time={res}")

        return wrapper

    return decorator


@measureTime("msec")
def dodaj(a, b):
    return a + b


print(dodaj(3, 5))
