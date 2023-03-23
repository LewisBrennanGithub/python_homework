from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Barry Feltz")
author_repository.save(author1)
author2 = Author("Ray Knockers")
author_repository.save(author2)

author_repository.select_all()

book_1 = Book("I Feltzumthin - Once", "Biography", author1)
book_repository.save(book_1)

book_2 = Book("Can't knock a day with Ray", "Biography", author2)
book_repository.save(book_2)