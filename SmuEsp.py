import os, signal, sys, csv
import imports.other.terminalsize as terminalsize
import imports.other.getch as getch
from pathlib import Path
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
        w.flushLines()
        if action == 't':
            test = Test(file, W, encoding, window=w)
            test.doTest()
            getch.getch()
            action = 'm'
        elif action == 'q':
            break;
        elif action == 'e':
            w.printWindow()
            w.setCursor(3)
            testset = TestSet(file, encoding)
            testset.addRowToSet()
            w.cursor = 5
            w.updateAndPrint(4, testset.sortAndSave())
            w.updateAndPrint(7, 'Enter - next   q - quit')
            next_row = getch.getch()
            action = 'm' if next_row is 'q' else 'e'
        elif action == 's':
            w.updateAndPrint(3, '  Enter database filename', centered=None)
            name = w.inputText(text = '  ', line=4)
            file = 'datasets/' + name
            if Path(file).is_file():
                w.updateAndPrint(3, 'File: ' + name + ' set as active')
            else:
                w.updateAndPrint(3, 'File does not exist, create an empty file?')
                w.updateAndPrint(7, 'y - yes   n - no   q - quit')
                yes_no = getch.getch()
                if yes_no == 'y':
                    with open(file, 'w', newline='', encoding=encoding) as out:
                        csv_out = csv.writer(out, delimiter=';')
                        csv_out.writerow(['query', 'response', 'rpt_count', 'timestamp'])
                        w.updateAndPrint(3, 'File ' + name + ' created and set as active')
                        getch.getch()
                elif yes_no == 'q':
                    file = ''
                else:
                    action = 's'
            action = 'm'        
        else:
            w.updateAndPrint(4, 'SMUESP 1.0.1')
            w.updateAndPrint(7, 't - training   e - edit database   s - select file   q - quit')
            action = getch.getch()

if __name__ == "__main__":
    main()
