class Book:


	def __init__(self, score: float):
		self.score = score
	
	def dump(self):
		print("Book with score {}".format(self.score))