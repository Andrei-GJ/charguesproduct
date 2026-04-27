# Problema 4: Diseñe un programa para calcular el valor final de un
# producto según su categoría.
# Requisitos:
# - Definir una constante IVA = 0.19. Ys
# - Solicitar el precio base del producto. YA 
# ✓ Si el precio ≤ 0, mostrar error y finalizar. YA
# - Solicitar el código de categoría: ya 
# ✓ Producto básico: no paga IVA.
# ✓ Producto estándar: paga IVA del 19%.
# ✓ Producto de lujo: paga IVA del 19% + recargo del 5%.
# - Si el código es inválido, mostrar error y finalizar. Ya 
# - Calcular y mostrar el valor final según la categoría. Ya

import os
import ast
from dotenv import load_dotenv

load_dotenv()

# Load env file
try:
    iva = float(os.getenv("iva"))
    charge = float(os.getenv("charge"))
    codeProduct = ast.literal_eval(os.getenv("codeProduct"))
    ruleProduct = ast.literal_eval(os.getenv("ruleProduct"))
except (ValueError, SyntaxError) as e:
    print(f"Error cargando configuración: {e}")

# Funtion to add gap in the console 
def gapConsole():
    print("\n")

productValue = float(input("Ingrese el valor del producto: "))

if productValue <= 0:
    print("Error: El valor del producto debe ser mayor a 0")
else:
    print(f"El valor del producto es: {productValue}")
    gapConsole()

for key, value in codeProduct.items():
    print(f"{key}: {value}")
    gapConsole()

categoryProduct = input("Ingrese el codigo de categoria: ").upper()
print (f'La categoria seleccionada fue {categoryProduct}')

if categoryProduct not in codeProduct:
    print ("Error : La categoria seleccionada no esta en la lista ")
    gapConsole()
    exit()
else:
    print (f'La categoria tiene la siguientes cantidad de reglas {ruleProduct[categoryProduct]}')

if categoryProduct not in ruleProduct:
    print ("Error : La regla seleccionada no esta en la lista ")
    gapConsole()
    exit()

rulesProduct = int(ruleProduct[categoryProduct])

match rulesProduct:
    case 0:
        print('El producto no tiene reglas su valor no cambia')
        print(productValue)
        gapConsole()
    case 1:
        print('Aplicando regla #1 solo se carga el iva')
        gapConsole()
        productIva = productValue * iva
        finalProduct = productValue + productIva
        print (f'El valor del producto es {productValue}')
        print(f'El valor del iva es de {iva}')
        gapConsole()
        print(f'El valor final del producto es de {finalProduct}')
        gapConsole()
    case 2:
        print("Aplicando regla #2 se carga el iva y el recargo")
        gapConsole()
        print (f'El valor del producto es {productValue}')
        print(f'El valor del iva es de {iva}')
        print(f'El valor del recargo es de {charge}')
        gapConsole()
        productIva = productValue * iva
        finalProduct = productValue + productIva
        chargeProduct = finalProduct * charge
        finalProduct = finalProduct + chargeProduct
        print (f'El valor final del producto es {finalProduct}')
        