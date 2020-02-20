

class Library:


	def __init__(self, signup_time, shipment_book_per_day):
		self.signup_time = signup_time
		self.shipment_book_per_day = shipment_book_per_day
		self.books = []

	def dump(self):
		print("--- --- ---")
		print("signup_time = {}".format(self.signup_time))
		print("shipment_book_per_day = {}".format(self.shipment_book_per_day))
		for book in self.books:
			book.dump()
		print("--- --- ---")

		