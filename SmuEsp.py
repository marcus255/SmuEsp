import os, signal, sys
import imports.other.terminalsize as terminalsize
from imports.Test import Test


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def handler(signum, frame):
    clear()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, handler)

    W, H = terminalsize.get_terminal_size()
    file = 'datasets/verbs_100.csv'
    encoding = '437'
    clear()
    test = Test(file, W, encoding)
    test.doTest()


# Adding new entries to dataset
# char = ''
# while (char != 'q'):
#    test.testset.addRowToSet()
#    char = input()

if __name__ == "__main__":
    main()

    # TBD:
    # comparison insensitive to accents
    # deriving classes from class Test
    # user will be able to define column mapping for test
    # class Window, testsets preview in this class
    # handle not allowed char exception on input
    # saving row immediately when user defines it
    # return to failed question when set finishes, as in duolingo
    # decrementing rpt_count along with forget curve, reset rpt_count
