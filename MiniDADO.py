# -*- coding: utf-8 -*-
"""

@author: kilde
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

import random

def byte2Per(nbyte):

	return nbyte*(1/255)

def generate_number(self):

	self.random_lblnumdado.text = str(random.randint(1,6))

class Dados(App):

	def btnaccion_press(self,obj):

		self.lblnumdado.text = str(random.randint(1,6))

		with self.lbltitulo.canvas:

			Color(byte2Per(34),0,byte2Per(159),1)

			Rectangle(pos=self.lbltitulo.pos, size=self.lbltitulo.size)
	
	def __init__(self,**kwargs):

		super().__init__(**kwargs)
		
	def build(self):

		gdl_principal = GridLayout(rows=3,cols=1)

		lbltitulo = Label(text='Aplicacion Dado')

		with lbltitulo.canvas:

			Color(byte2Per(34),0,byte2Per(159),1)

			Rectangle(pos=lbltitulo.pos, size=lbltitulo.size)

		self.lbltitulo = lbltitulo

		gdl_principal.add_widget(lbltitulo)

		gdl_medio = GridLayout(cols=2)

		lblresultado = Label(text='El Resultado es: ')

		gdl_medio.add_widget(lblresultado)

		lblnumdado = Label(text="")

		gdl_medio.add_widget(lblnumdado)

		gdl_principal.add_widget(gdl_medio)

		btnaccion = Button(text="Presionanme!!!")

		gdl_principal.add_widget(btnaccion)

		btnaccion.bind(on_press = self.btnaccion_press)

		self.gdl_principal = gdl_principal

		self.lblnumdado = lblnumdado

		return gdl_principal

if __name__ == '__main__':
	D = Dados()
	D.run()
