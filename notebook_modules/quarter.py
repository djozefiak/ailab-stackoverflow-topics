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
	def make_quarter(year, quarter):
		startMonth = 3 * quarter - 2
		start = dt.datetime(year, startMonth, 1)
		if startMonth == 10:
			end = dt.datetime(year + 1, 1, 1)
		else:
			endMonth = startMonth + 3
			end = dt.datetime(year, endMonth, 1)
		return Quarter(year, quarter, start, end)

	@staticmethod
	def make_quarters(startYear, endYear):
		quarters = []
		for y in range(startYear, endYear):
			for q in [1, 2, 3, 4]:
				quarters.append(Quarter.make_quarter(y, q))
		return quarters
