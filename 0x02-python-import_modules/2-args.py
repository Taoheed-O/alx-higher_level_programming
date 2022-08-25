#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1

    if a == 0:
        print("{} arguments.".format(a))
    else:
        print("{} arguments:".format(a))

    if a >= 1:
        for i, arg in enumerate(sys.argv):
            if i != 0:
                print("{}: {}".format(i, arg))
