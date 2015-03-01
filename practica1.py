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
	cx_random1 = random.randint(50, 100)
	cy_random1 = random.randint(50, 100)
	r_random1 = random.randint(20, 50)

	cx_random2 = random.randint(50, 100)
	cy_random2 = random.randint(50, 100)
	r_random2 = random.randint(20, 50)

	cx_random3 = random.randint(50, 100)
	cy_random3 = random.randint(50, 100)
	r_random3 = random.randint(20, 50)

	return 	'''
			<svg height="200" width="200"> 
				<circle cx="%s" cy="%s" r="%s" stroke="black" stroke-width="3" fill="red" /> 
				<circle cx="%s" cy="%s" r="%s" stroke="white" stroke-width="3" fill="blue" /> 
				<circle cx="%s" cy="%s" r="%s" stroke="black" stroke-width="3" fill="green" /> 
			</svg> 
			''' % (cx_random1, cy_random1, r_random1, cx_random2, cy_random2, r_random2, cx_random3, cy_random3, r_random3)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
