#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_args = len(sys.argv) - 1

    if len_args == 0:
        print("{} arguments".format(len_args))
    elif len_args == 1:
        print("{} argument".format(len_args))
    else:
       print("{} arguments".format(len_args))

    if len_args >= 1:
        len_args = 0
        for args in sys.argv:
            if len_args != 0:
                print("{}: {}".format(len_args, args))
            len_args += 1
