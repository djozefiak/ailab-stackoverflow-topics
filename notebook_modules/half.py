import datetime as dt

class Half:
	def __init__(self, year, half, start, end):
		self.year = year
		self.number = half
		self.start = start
		self.end = end

	def __str__(self):
		return f"{self.year}-H{self.number}"

	@staticmethod
	def make_half(year, half):
		startMonth = 6 * half - 5
		start = dt.datetime(year, startMonth, 1)
		if startMonth == 7:
			end = dt.datetime(year + 1, 1, 1)
		else:
			endMonth = startMonth + 6
			end = dt.datetime(year, endMonth, 1)
		return Half(year, half, start, end)

	@staticmethod
	def make_halves(startYear, endYear):
		halves = []
		for y in range(startYear, endYear):
			for h in [1, 2]:
				halves.append(Half.make_half(y, h))
		return halves

