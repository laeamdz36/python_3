"""Modulo par testear funciones"""
import practice_class.classes_1 as pc
import practice_class.arith as ari

# Execution of function from package "practice_class"
pc.load_module()

# execution of function sumar from arith modules insidde practice_class package
ari.sumar(10,12)

# execution of function that call comm module inside practice package
pc.get_comm()

luisin = pc.Person("Luisin")
