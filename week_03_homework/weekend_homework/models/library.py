from models.book import *

book1 = Book("book1", "author1", "genre1", False)
book2 = Book("book2", "author2", "genre2", False)
book3 = Book("book3", "author3", "genre3", False)

book_list = [book1, book2, book3]

def add_new_book(book):
    book_list.append(book)

# def change_checkout_status():




    