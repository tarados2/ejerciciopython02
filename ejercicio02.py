# -*- coding: utf-8 -*-
"""
 Mostrar el precio del IVA de un producto con un valor puesto por usuario y su precio final.
"""

IVA = 0.21
precioProducto = input("Introduce un número entero: ")
precioIVA = precioProducto * IVA
print("El precio del IVA es", precioIVA, "€")
 
print("El precio final es", (precioIVA+precioProducto) ,"€")
