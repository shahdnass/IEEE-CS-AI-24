library_catalogue = {}

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    publication_year = int(input("Enter the publication year of the book: "))
    return {"title": title, "author": author, "publication_year": publication_year}

num_books = int(input("How many books do you want to add to the catalogue? "))

for i in range(num_books):
    book_key = "book" + str(i + 1)
    library_catalogue[book_key] = add_book()

print("Library Catalogue:")
for key, book in library_catalogue.items():
    print(key, ":", book)

