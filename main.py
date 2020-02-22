from models import *
from write_file import *

LIBRARY_INPUT = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
#LIBRARY_INPUT = ["a_example.txt"]

for l in LIBRARY_INPUT:
  print(f"Calculating file: {l}")
  data = Data(l)

  # print(data.books)
  # for lib in data.libraries:
    # for i in range(len(lib.books)):
      # print(f"Book {lib.books[i]} with score {data.books[lib.books[i]]}")
    # print("\n")

  #for lib in data.libraries:
  #  print(lib.id)
  
  data.libraries.sort(key = lambda x : x.weight, reverse=True)
  
  final_libraries = []

  static_libraries = data.libraries

  for i in range(len(data.libraries)):
    lib = data.libraries[i]
    if not lib.sorted:
      lib.weight = data.calc_weight(lib, data.books)
      data.libraries.sort(key = lambda x : x.weight, reverse=True)
      lib.books.sort(key = lambda x : int(data.books[x]), reverse=True)
      data.number_of_days -= lib.signup
      if data.number_of_days >= 0:
        final_libraries.append(lib)
        lib.sorted = True
        for book in lib.books:
          data.books[book] = 0

  answer_file = l.split('.')[0] + "_ans3.txt"
  write_file(final_libraries, answer_file)
print("Complete")
