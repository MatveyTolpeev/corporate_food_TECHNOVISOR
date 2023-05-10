import traceback

from django.http import HttpResponse


def out_green(text):
    print("\033[4m\033[32m {}" .format(text))
    print("\033[37m {}".format(""))


def out_yellow(text):
    print("\033[4m\033[33m {}" .format(text))


def out_blue(text):
    print("\033[4m\033[34m {}" .format(text))


def color_decorator(func):
    def wrapper(*args, **kwargs):
        print("\033[4m\033[33m {}".format("[+] start {}".format(func.__name__)))
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"\033[4m\033[34m Error in function {func.__name__}: {e}")
            traceback.print_exc()
            print("\033[37m {}".format(""))
            return HttpResponse("Exception, check traceback")
        if result is not None:
            print("\033[4m\033[33m {}" .format("[++] end {}".format(func.__name__)))
            print("\033[37m {}".format(""))
        else:
            print("\033[4m\033[33m {}" .format("[++] end {}".format(func.__name__)))
            print("\033[37m {}".format(""))
        return result
    return wrapper
