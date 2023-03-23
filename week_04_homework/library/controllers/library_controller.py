from flask import Flask, render_template, request, redirect
from repositories import book_repository
from repositories import author_repository
from models.book import Book
from models.author import Author

from flask import Blueprint

library_blueprint = Blueprint("library", __name__)

# INDEX
# GET '/library'
@library_blueprint.route("/library")
def library():
    library = book_repository.select_all() # NEW
    return render_template("library/index.html", library = library)

# # NEW
# # GET '/library/new'
@library_blueprint.route('/library/new/')
def new_book():
    all_authors = author_repository.select_all()
    return render_template("library/new.html", library=all_authors)

# # CREATE
# # POST '/tasks'
@library_blueprint.route('/library', methods = ['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, genre, author)
    book_repository.save(book)
    return redirect('/library')

# SHOW
# GET '/tasks/<id>'
@library_blueprint.route('/library/<id>', methods = ['GET'])
def view_task(id):
    book = book_repository.select(id)
    return render_template("library/book.html", book=book)

# EDIT
# GET '/tasks/<id>/edit'
@library_blueprint.route('/library/<id>/edit', methods = ['GET'])
def edit_task(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("library/edit.html", book=book, authors=authors)

# UPDATE
# PUT '/tasks/<id>'
@library_blueprint.route("/library/<id>", methods=['POST'])
def update_task(id):
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, genre, author, id)
    book_repository.update(book)
    return redirect('/library')

# DELETE
# DELETE '/tasks/<id>'
@library_blueprint.route("/library/<id>/delete", methods = ['POST'])
def delete_task(id):
    book_repository.delete(id)
    return redirect('/library')



