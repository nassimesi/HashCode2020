import sys
from Book import Book 
from Library import Library

days: int = 0
books: [Book] = []
libraries: [Library] = []

def dump_books():
	for book, i in zip(books, range(len(books))):
		print("%d	%f".format(i, book.score))

def parse_books(line):
	line = line.split()
	for score, i in zip(line, range(len(line))):
		score = float(score)
		books.append(Book(score))
		
	print("There are {} books".format(len(books)))

def parse_libraries(inpt):
	meta = inpt.readline()
	while meta:
		meta = meta.split()
		library: Library = Library(float(meta[1]), float(meta[2]))
		libraries.append(library)
		booksindexs = inpt.readline().split()
		for index in booksindexs:
			index = int(index)
			library.books.append(books[index])
		
		meta = inpt.readline()

	for library in libraries:
		library.dump()

def parse(inpt):
	line = inpt.readline()
	meta = line.split()

	days = int(meta[2])
	print("There are {} days".format(days))

	line = inpt.readline()
	parse_books(line)

	parse_libraries(inpt)


if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("python3 hashcode <inputfile> <outputfile>")
		sys.exit(84)


	inpt = open(sys.argv[1], "r")
	parse(inpt)

	output = open(sys.argv[2], "w")
	
	print("Hello world in Hashcode")