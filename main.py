import os
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = 'home'
    return render_template('home.html',title=title)

@app.route('/mode')
def mode():
    title = 'change background'
    return render_template('changeBg.html',title=title)

@app.route('/checkout')
def chart():
    title = 'checkout'
    return render_template('checkout.html',title=title)

@app.route('/biodata')
def form():
    title = 'biodata'
    return render_template('form.html',title=title)

@app.route('/loop')
def loop():
    title = 'looping'
    return render_template('looping.html',title=title)

@app.route('/raport')
def raport():
    title = 'raport'
    return render_template('lulusTidak.html',title=title)

@app.route('/bilangan')
def bil():
    title = 'type bilangan'
    return render_template('ganjilGenap.html',title=title)

