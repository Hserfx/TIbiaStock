


def other_func(a, b=None, c=None, d=None):
    print(a, b, c, d)

def func(a, **kwargs):
    other_func(a, **kwargs)


func(2, b=3, d=2)

