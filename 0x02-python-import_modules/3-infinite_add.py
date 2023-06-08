#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_args = len(sys.argv)
    sum = 0
    int(sum)
    if len_args == 1:
        print("{}".format(sum))
    else:
        counter = 1
        while counter < len_args:
            sum += int(sys.argv[counter])
            counter += 1
        print("{}".format(sum))
