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
			for q in [1, 2, 3, 4]:
				startMonth = 3 * q - 2
				start = dt.datetime(y, startMonth, 1)
				if startMonth == 10:
					end = dt.datetime(y + 1, 1, 1)
				else:
					endMonth = startMonth + 3
					end = dt.datetime(y, endMonth, 1)
				quarter = Quarter(y, q, start, end)
				quarters.append(quarter)
		return quarters
