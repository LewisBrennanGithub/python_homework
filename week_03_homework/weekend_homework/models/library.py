from models.book import *

book1 = Book("book1", "author1", "genre1")
book2 = Book("book2", "author2", "genre2")
book3 = Book("book3", "author3", "genre3")

book_list = [book1, book2, book3]

def add_new_book(book):
    book_list.append(book)

# def checkout_book(book_title):
#     for book in book_list:
#         if book.title == book_title:
#             book.checked_out = True
#             return True
#     return False




    