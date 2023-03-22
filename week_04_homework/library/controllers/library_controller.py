from flask import Flask, render_template, request, redirect
from repositories import book_repository
from repositories import author_repository
from models.book import Book
from models.author import Author

from flask import Blueprint

tasks_blueprint = Blueprint("tasks", __name__)