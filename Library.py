
from Book import Book 

class Library:


	def __init__(self, id, signup_time, shipment_book_per_day):
		self.id = id
		self.signup_time = signup_time
		self.shipment_book_per_day = shipment_book_per_day
		self.books = []
		self.books_shiped = []
		self.forbiden_books = 0;

	def dump(self):
		print("--- --- ---")
		print("signup_time = {}".format(self.signup_time))
		print("shipment_book_per_day = {}".format(self.shipment_book_per_day))
		for book in self.books:
			book.dump()
		print("--- --- ---")

	def books_sum(self) -> float:
		tt = 0
		for book in self.books:
			tt += book.score
		return tt

	def ship_books_for_day(self):
		quantity = self.shipment_book_per_day
		self.books.sort(key=lambda b: b.score)
		self.books.reverse()
		while quantity != 0 and len(self.books) > 0:
			self.books_shiped.append(self.books.pop(0))
			quantity = quantity - 1
		pass
