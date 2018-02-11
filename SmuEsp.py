import os, signal, imports.other.terminalsize as terminalsize
from imports.Test import Test

def handler(signum, frame):
	os.system('cls')
	os._exit(0)

def main():

	signal.signal(signal.SIGINT, handler)
	
	W, H = terminalsize.get_terminal_size()	
	file = 'datasets/verbs_100.csv'
	encoding = '437'
	os.system('chcp ' + encoding + ' >nul')
	os.system('cls')

	test = Test(file, W, encoding)
	test.doTest()
	
	## Adding new entries to dataset
	#char = ''
	#while (char != 'q'):
	#	test.testset.addRowToSet()
	#	char = input()

if __name__ == "__main__":
	main()


# TBD:
# comparison insensitive to accents
# deriving classes from class Test 
# user will be able to define column mapping for test
# class Window, testsets preview in this class
# handle not allowed char exception on input (i.e. 'ÍÓ')
# saving row immediately when user defines it
# return to failed question when set finishes, as in duolingo
# decrementing rpt_count along with forget curve, reset rpt_count