import sys
import inspect

def debug(*args):
    cf = inspect.currentframe()

    stack = inspect.stack()[1][1]
    segs = stack.split("/")
    if len(segs) > 4:
        segs = segs[(len(segs) - 4):]
    back = cf.f_back
    print("[debug][%s:%d]" % ("/".join(segs), back.f_lineno), *args, file=sys.stdout)

def error(*args):
    cf = inspect.currentframe()

    stack = inspect.stack()[1][1]
    segs = stack.split("/")
    if len(segs) > 4:
        segs = segs[(len(segs) - 4):]
    back = cf.f_back
    print("[error][%s:%d]" % ("/".join(segs), back.f_lineno), *args, file=sys.stdout)