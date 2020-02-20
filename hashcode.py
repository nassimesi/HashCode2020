import sys
from Book import Book 
from Library import Library
from rentability import rentability

days: int = 0
books: [Book] = []
libraries: [Library] = []

def parse_books(line):
	line = line.split()
	for score, i in zip(line, range(len(line))):
		score = float(score)
		books.append(Book(i, score))
		
	print("There are {} books".format(len(books)))

def parse_libraries(inpt):
	meta = inpt.readline()
	id = 0
	while meta:
		meta = meta.split()
		if len(meta) == 3:
			library: Library = Library(id, float(meta[1]), float(meta[2]))
			libraries.append(library)
			booksindexs = inpt.readline().split()
			for index in booksindexs:
				index = int(index)
				library.books.append(books[index])
			
			id += 1
		else:
			booksindexs = inpt.readline().split()

		meta = inpt.readline()

	# for library in libraries:
	# 	library.dump()

def parse(inpt) -> int:
	line = inpt.readline()
	meta = line.split()

	days = int(meta[2])
	print("There are {} days".format(days))

	line = inpt.readline()
	parse_books(line)

	parse_libraries(inpt)
	return days


if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("python3 hashcode <inputfile> <outputfile>")
		sys.exit(84)


	inpt = open(sys.argv[1], "r")
	days = parse(inpt)
	output = open(sys.argv[2], "w")
	rentability(books, libraries, days, output)
	
	print("Hello world in Hashcode")