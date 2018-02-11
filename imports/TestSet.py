import csv, random, re

class TestSet:

	data      = []     # data rows without header row and learned rows
	learned   = []     # data rows with rpt_count above threshold
	threshold = 5      # threshold to exclude already memorised phrases
	fname     = ''     # filename of csv file with phrases database
	rows      = 0      # row count in 'data' list
	cols      = 0      # csv file columns
	to_redo   = []     # rows failed in first test run 
	encoding  = 'utf8' # encoding page for OEM-US (spanish characters)
	
	def __init__(self, filename, enc):
		if enc is not None: self.encoding = enc
		self.fname = filename
		with open(filename, 'r', encoding=self.encoding) as f:
			reader = csv.reader(f,  delimiter=';')
			self.data = list(reader)
		self.header = self.data[0]
		self.cols = len(self.header)
		del self.data[0]
		for row in self.data:
			if int(row[self.cols - 2]) > self.threshold:
				self.learned.append(row)
		i = 0
		while i < len(self.data):
			if int(self.data[i][self.cols - 2]) > self.threshold:
				del self.data[i]
				i -= 1
			i += 1
		self.rows = len(self.data)
		random.shuffle(self.data)
	
	def getDataString(self):
		data_str = ''
		for row in self.data:
			for i in range (0, self.cols - 1):
				data_str += row[i] + '-'
			data_str += row[self.cols - 1] + '\n'
		return data_str
	
	def sortAndSave(self, filename = None):
		filename = filename if filename is not None else self.fname
		self.data += self.learned
		self.data.sort(key=lambda tup: tup[0])
		self.data.insert(0,self.header)
		with open(filename,'w',newline='',encoding=self.encoding) as out:
			csv_out=csv.writer(out,  delimiter=';')
			for row in self.data:
				csv_out.writerow(row)
		return 'Your progress has been saved in ' + filename
	
	def addRowToSet(self):
		row = [0] * self.cols
		for i in range (0, self.cols - 2):
			text = input('  ' + (self.header[i]) + ': ')
			row[i] = text.encode(self.encoding).decode(self.encoding, 'surrogateescape')
		row[self.cols - 2] = '0'
		row[self.cols - 1] = '0.0'
		self.data.append(row)
	
	def resetRptCount(self):
		print() # TBD