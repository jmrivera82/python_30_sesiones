#!/usr/bin/env python3
"""
hola_mundo.py - mi primer script python profesional
"""

def saludar (nombre:str) -> str:
	"""devuelve un saludo formateado."""
	return f"Hola, {nombre}! Bienvenido a Python."

if __name__ == "__main__":
	mensaje = saludar ("Mundo")
	print(mensaje)


