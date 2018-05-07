import sys


# Gather our code in a main() function
def main():
    print('hello world', sys.argv[0])
    print(len(sys.argv))
    # command lines args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself  and can be ingored


# standard boilerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()
