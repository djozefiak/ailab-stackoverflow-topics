import datetime as dt

class Quarter:
	def __init__(self, year, quarter, start, end):
		self.year = year
		self.number = quarter
		self.start = start
		self.end = end

	def __str__(self):
		return f"{self.year}-Q{self.number}"

	@staticmethod
	def make_quarters(startYear, endYear):
		quarters = []
		for y in range(startYear, endYear):
			for q in range(1, 5):
				endMonth = 3 * q
				startMonth = endMonth - 2
				endDay = 31
				if endMonth == 6 or endMonth == 9:
					endDay = 30
				start = dt.datetime(y, startMonth, 1)
				end = dt.datetime(y, endMonth, endDay)
				quarter = Quarter(y, q, start, end)
				quarters.append(quarter)
		return quarters
