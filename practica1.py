# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, Response
import random
app = Flask(__name__)

@app.route('/')
def api_root():
	mensaje = 'Welcome'
	return Response(mensaje, status=200, mimetype='text/plain')

@app.route('/hola')
def api_home():
	mensaje = 'Hola -cañón-'
	return Response(mensaje, status=200, mimetype='text/plain')

@app.route('/imagen')
def api_imagen():
	mensaje = '<img src=' + url_for('static',filename='img/imagen.jpg') + '>'
	return Response(mensaje, status=200, mimetype='image/jpg')

@app.route('/hola_pepe')
def api_pepe():
	mensaje = 'Hola <b> pepe</b>'
	return Response(mensaje, status=200, mimetype='text/html')

@app.route('/pagina')
def api_pagina():
	mensaje = render_template('pagina.html')
	return Response(mensaje, status=200, mimetype='text/html')

@app.route('/circulos_varios')
def api_circulos():
	randoms = [random.randrange(50,200) for i in range(9)]
	mensaje = render_template(	'circulos.xml', 
								cx1=randoms[0], cy1=randoms[1], r1=randoms[2], 
								cx2=randoms[3], cy2=randoms[4], r2=randoms[5], 
								cx3=randoms[6], cy3=randoms[7], r3=randoms[8])
	return Response(mensaje, status=200, mimetype='image/svg+xml')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
