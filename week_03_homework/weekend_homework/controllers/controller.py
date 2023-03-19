from flask import render_template, request, redirect
from app import app
from models.library import *
from models.book import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/library')
def library_index():
    return render_template('index.html', title = "generic library", book_collection = book_list)

@app.route('/library/<index>')
def single_book(index):
  chosen_book = book_list[int(index)]
  return render_template('bookinfo.html', book=chosen_book)

@app.route('/library', methods=['POST'])
def add_book():
  bookTitle = request.form['title']
  bookAuthor = request.form['author']
  bookGenre = request.form['genre']
  newBook = Book(title=bookTitle, author=bookAuthor, genre=bookGenre, checked_out = False)
  add_new_book(newBook)
  return redirect('/library')

@app.route('/delete/<int:index>')
def delete_book(index):
    book_list.pop(index)
    return redirect('/library')

@app.route('/checkout_book/<book_title>', methods=['POST'])
def checkout_book(book_title):
    for book in book_list:
        if book.checked_out:
            book.checked_out = False
            return redirect('/library')
        else:
            book.checked_out = True
            return redirect('/library')
    return redirect('/library')

# @app.route('/checkout_book/<book_title>', methods=['POST'])
# def checkout_book(book_title):
#     for book in book_list:
#         # if book.title == book_title:
#             if book.checked_out:
#                 book.checked_out = False
#                 return redirect('/library')
#             else:
#                 book.checked_out = True
#                 return redirect('/library')
#     # return f'Could not find book with title: {book_title}.'
#     return redirect('/library')

   