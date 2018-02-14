import os, signal, sys
import imports.other.terminalsize as terminalsize
import imports.other.getch as getch
from imports.Test import Test
from imports.TestSet import TestSet
from imports.Window import Window
from imports.Colors import bc

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def handler(signum, frame):
    clear()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, handler)

    W, H = terminalsize.get_terminal_size()
    file = 'datasets/verbs_2.csv'
    encoding = '437'
    clear()
    
    w = Window([''] * 7, W - 1)
    
    action = 'm'
    while True:
        if action == 't':
            w.flushLines()
            test = Test(file, W, encoding, window=w)
            test.doTest()
            action = 'm'
        elif action == 'q':
            break;
        elif action == 'e':
            w.flushLines()
            w.printWindow()
            w.setCursor(3)
            testset = TestSet(file, encoding)
            testset.addRowToSet()
            w.cursor = 5
            w.updateAndPrint(4, testset.sortAndSave())
            w.updateAndPrint(7, 'Enter - next   q - quit')
            next_row = getch.getch()
            action = 'm' if next_row is 'q' else 'e'
        else:
            w.updateAndPrint(4, 'SMUESP 1.0.1')
            w.updateAndPrint(7, 't - training   e - edit database   q - quit')
            action = getch.getch()

if __name__ == "__main__":
    main()
