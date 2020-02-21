class Library():
  def __init__(self, id, book_amount, signup, shipping, books):
    self.id : int = int(id)
    self.book_amount : int = int(book_amount)
    self.signup : int = int(signup)
    self.shipping : int = int(shipping)
    self.books : List = books

class Data():
  def __init__(self, file):
    f = open(file, "r")
    first_line = f.readline()
    nums = first_line.split(' ')

    self.total_books = int(nums[0])
    self.total_libraries = int(nums[1])
    self.number_of_days = int(nums[2])

    second_line = f.readline()
    book_data = second_line.split(' ')
    self.books = []

    for book in book_data:
      self.books.append(book)

    self.libraries = []
    
    c = 0
    line = f.readline()
    while (line != '' and line != '\n'):
      lib_data = line.split(' ')
      line = f.readline()
      data = line.split(' ')

      lib_books = []
      for i in data:
        lib_books.append(self.books[int(i)])

      lib = Library(c, lib_data[0], lib_data[1], lib_data[2], lib_books)
      c += 1
      #lib.sort() #???
      self.libraries.append(lib)


      line = f.readline()

    f.close()
