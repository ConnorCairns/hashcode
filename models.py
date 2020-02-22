class Library():
  sorted = False
  def __init__(self, id, book_amount, signup, shipping, books, weight):
    self.id : int = int(id)
    self.book_amount : int = int(book_amount)
    self.signup : int = int(signup)
    self.shipping : int = int(shipping)
    self.books : List = books
    self.weight : int = weight

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
        lib_books.append(int(i))

      lib_books.sort(key = lambda x : self.books[x], reverse=True)

      #weight = self.calc_weight(self.books, lib_books, lib_data[1], lib_data[2])
      weight = 0
      lib = Library(c, lib_data[0], lib_data[1], lib_data[2], lib_books, weight)
      lib.weight = self.calc_weight(lib, self.books)
      
      c += 1
      #lib.sort() #???
      self.libraries.append(lib)


      line = f.readline()

    f.close()

  #def calc_weight(self, book_scores, lib_books, signup, shipping):
  def calc_weight(self, lib, book_scores):
    total_score = 0
    for book in lib.books:
      total_score += int(book_scores[book])
    
    return (total_score/int(lib.signup))*int(lib.shipping)
