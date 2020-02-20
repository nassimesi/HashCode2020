class Book:


	def __init__(self, id: int, score: float):
		self.score = score
		self.id = id
	
	def dump(self):
		print("Book with score {}".format(self.score))
