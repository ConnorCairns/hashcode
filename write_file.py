def write_file(libraries, filename):
  f = open(filename, "w")

  # count = 0
  # if libraries[len(libraries) - 1].books == 0:
    # count += 1
  f.write(str(len(libraries)) + "\n")

  for l in libraries:
    #if len(l.books) != 0:
      f.write(f"{l.id} {len(l.books)}\n")
      new_books = []
      for book in l.books:
          new_books.append(str(book))
      final_str = " ".join(new_books) + "\n"
      f.write(final_str)

  f.close()