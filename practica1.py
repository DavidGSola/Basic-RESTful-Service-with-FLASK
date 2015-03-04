# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template
import random
app = Flask(__name__)

@app.route('/')
def api_root():
	return 'Welcome'

@app.route('/hola')
def api_home():
	return 'Hola -cañón-'

@app.route('/imagen')
def api_imagen():
	return '<img src=' + url_for('static',filename='img/imagen.jpg') + '>'

@app.route('/hola_pepe')
def api_pepe():
	return 'Hola <b> pepe</b>'

@app.route('/pagina')
def api_pagina():
	return render_template('pagina.html')

@app.route('/circulos_varios')
def api_circulos():
	randoms = [random.randrange(50,200) for i in range(9)]

	return 	'''
			<svg height="500" width="500"> 
				<circle cx="%s" cy="%s" r="%s" stroke="black" stroke-width="3" fill="red" /> 
				<circle cx="%s" cy="%s" r="%s" stroke="white" stroke-width="3" fill="blue" /> 
				<circle cx="%s" cy="%s" r="%s" stroke="black" stroke-width="3" fill="green" /> 
			</svg> 
			''' % (randoms[0],randoms[1],randoms[2],randoms[3],randoms[4],randoms[5],randoms[6],randoms[7],randoms[8])

if __name__ == '__main__':
	app.run(host='0.0.0.0')
