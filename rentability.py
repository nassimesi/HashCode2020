from Book import Book 
from Library import Library

def proceed(libraries: [Library], days: int, output):
	outlibs: [Library] = []
	
	print("Proceed {} days".format(days))
	while days != 1:
		# if len(libraries) != 0:
			# libraries[0].dump()

		reorderedlibraries = sorted(libraries,key=lambda lib: lib.books_sum() * lib.shipment_book_per_day * (1 / lib.signup_time) * (1 / (lib.libb.forbiden_books+1)))
		reorderedlibraries.reverse()

		if len(libraries) != 0 and libraries[0].signup_time == 0:
			outlibs.append(libraries.pop(0))

		for lib in outlibs:
			lib.ship_books_for_day()

		for libb in libraries:
			libb.forbiden_books += len((set(libb.books) & set(lib.books_shiped)))


		if len(libraries) != 0:
			libraries[0].signup_time -= 1

		days -= 1



	print(str(len(outlibs)), file=output)
	for lib in outlibs:
		print("{} {}".format(lib.id, len(lib.books_shiped)), file=output)
		for book in lib.books_shiped:
			print("{} ".format(book.id), end='', file=output)
		print(file=output)


def rentability(books: [Book], libraries: [Library], days: int, output):
	reorderedlibraries: [Library] = []

	#reorderedlibraries = sorted(libraries, key=lambda lib: lib.books_sum() * lib.shipment_book_per_day * (1 / lib.signup_time))
	#reorderedlibraries.reverse()
	# for library in reorderedlibraries:
	# 	print(libraries.index(library))
	
	proceed(reorderedlibraries, days, output)
