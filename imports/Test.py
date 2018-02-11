import colorama, time, re
from imports.Colors import bc
from imports.Window import Window
from imports.TestSet import TestSet

# CSV file header indices
QUERY    = 0
RESPONSE = 1
RTP_CNT  = 2
TS       = 3

class Test:

	testset = TestSet
	w = Window
	term_width = 0  # console window width
	filename   = '' # csv filename
	completed  = 0  # number of curently iterated records
	passed     = 0  # passed records
	failed     = 0  # failed records
	max_rows   = 20 # max number of records for single trenning
	
	def __init__(self, test_filename, width, encoding = None, max = None):
		if max is not None: self.max_rows = max
		self.term_width = width
		colorama.init()
		self.w = Window([''] * 7, self.term_width - 1)
		self.w.updateAndPrint(4, 'SMU ESPAÑOL 1.0.1', centered = True)
		self.w.inputText()
		self.w.updateAndPrint(4, '')
		self.filename = test_filename
		self.testset = TestSet(self.filename, encoding)
		if self.testset.rows < self.max_rows: self.max_rows = self.testset.rows
			
	def doTest(self):
		if self.max_rows == 0:
			self.w.updateAndPrint(4, 'No records found for practising')
			return
		else:
			self.w.updateAndPrint(4, 'Starting with ' + str(self.max_rows) + ' of ' + str(self.testset.rows) + ' records from ' + self.filename)
		self.w.inputText()
		self.w.updateLine(4, '')
		self.w.updateAndPrint(6, self.getProgressBar() + bc.ENDC + ' ' + self.getProgress())
		for row, i in zip(self.testset.data, range(0, self.max_rows)):
			row = self.askRow(row)
		end_str = 'Your score is {}/{} '.format(self.passed, self.max_rows) + self.getScore()
		self.w.updateLine(4, end_str, centered = True)
		self.w.updateAndPrint(6, '')
		self.w.inputText()
		self.w.updateAndPrint(4, self.testset.sortAndSave())
		
	def askRow(self, row):
		answer = self.w.inputText('  ' + row[QUERY] + ': ', 2, no_offset = True)
		expected = row[RESPONSE]
		wrong_ans = False
		regex = re.compile('[¿¡?!]')
		while regex.sub('', answer.lower()) != regex.sub('', expected.lower()):
			wrong_ans = True
			self.w.updateAndPrint(4, bc.FGBRED + 'Wrong!' + bc.ENDC + ' Correct answer is: ' + bc.FGBCYAN + expected + bc.ENDC)
			if int(row[RTP_CNT]) > 0:
				row[RTP_CNT] = str(int(row[RTP_CNT]) - 1)
			self.w.inputText()
			self.w.updateAndPrint(4, '')
			answer = self.w.inputText('  ' + row[QUERY] + ': ', 2, no_offset = True)
			
		self.w.updateLine(4, bc.FGBGREEN + 'Correct!' + bc.ENDC)
		if not wrong_ans:
			self.passed += 1
			row[RTP_CNT] = str(int(row[RTP_CNT]) + 1)
		row[TS] = time.time()
		self.completed += 1
		self.failed = self.completed - self.passed
		self.w.updateAndPrint(6, self.getProgressBar() + bc.ENDC + ' ' + self.getProgress())
		self.w.inputText()
		self.w.updateAndPrint(4, '')
		return row
		
	def getProgress(self):
		return '{:0.0f}%'.format(100*self.completed/self.max_rows)
		
	def getScore(self):
		return '({:0.0f}%)'.format(100*self.passed/self.max_rows)
	
	def getProgressBar(self):
		out_str = ''
		w = self.term_width - 8
		pre_pass = self.passed / self.max_rows * w
		pre_fail = self.failed / self.max_rows * w
		post = w - (pre_pass + pre_fail)
		for i in range(0, int(pre_pass)):
			out_str += bc.FGBGREEN + '█'
		for i in range(0, int(pre_fail)):
			out_str += bc.FGBRED + '█'
		for i in range(0, int(post)):
			out_str += bc.FGBCYAN + '░' + bc.ENDC
		return out_str