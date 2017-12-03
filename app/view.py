# -*-coding:utf-8-*-
from app import app
from flask import render_template
from flask import request, redirect, g
from flask import url_for, jsonify, abort

@app.route('/', methods = ['GET'])
def root_path():
    return redirect(url_for('main_page'))

@app.route('/index', methods = ['GET'])
def main_page():
    return render_template('index.html')
