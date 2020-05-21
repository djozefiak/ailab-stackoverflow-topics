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
	def make_halves(startYear, endYear):
		halves = []
		for y in range(startYear, endYear):
			for h in [1, 2]:
				startMonth = 6 * h - 5
				start = dt.datetime(y, startMonth, 1)
				if startMonth == 7:
					end = dt.datetime(y + 1, 1, 1)
				else:
					endMonth = startMonth + 6
					end = dt.datetime(y, endMonth, 1)
				half = Half(y, h, start, end)
				halves.append(half)
		return halves

