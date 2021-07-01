import sys

if sys.version[0] == "2":
    exit("\n    domHttpx is not supported for python 2.x\n")

from domHttpx.cli import main

if __name__ == '__main__':
    main()