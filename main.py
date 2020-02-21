from models import *
from write_file import *

LIBRARY_INPUT = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
#LIBRARY_INPUT = ["a_example.txt"]

for l in LIBRARY_INPUT:
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

  for lib in data.libraries:
    data.number_of_days -= lib.signup
    if data.number_of_days >= 0:
      final_libraries.append(lib)

  answer_file = l.split('.')[0] + "_ans.txt"
  write_file(final_libraries, answer_file)
