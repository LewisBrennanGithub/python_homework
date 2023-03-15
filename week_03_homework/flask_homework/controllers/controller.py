from flask import render_template

from app import app
from models.tv_shop import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', order_list = orders)

@app.route('/orders/<id>')
def order(id):
    return render_template('order.html', title='Order', order = orders[int(id)])