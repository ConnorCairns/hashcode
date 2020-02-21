from models import *
from write_file import *

#LIBRARY_INPUT = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
LIBRARY_INPUT = ["a_example.txt"]

for l in LIBRARY_INPUT:
  data = Data(l)

  print(data.books)
  for lib in data.libraries:
    print(lib.books)