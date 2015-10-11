class previous_tracks():
	max_size = 100
	def __init__(self):
		self.list = []
		self.pos = 0

	def add(self, track):
		self.list.append(track)
		self.pos += 1
		if self.pos > self.max_size:
			self.list = self.list[:100]

	def get_prev(self):
		if self.pos < 0:
			return None
		if len(self.list) == 0:
			return None
		prev = self.list.pop()
		if prev:
			self.pos -= 1
		return prev 



