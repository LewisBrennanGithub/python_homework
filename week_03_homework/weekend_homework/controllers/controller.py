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
  newBook = Book(title=bookTitle, author=bookAuthor, genre=bookGenre)
  add_new_book(newBook)
  return redirect('/library')

@app.route("/library/<index>", methods=["POST"])
def book_delete(index):
    remove_named_book(int(index))
    return redirect("/library")

   