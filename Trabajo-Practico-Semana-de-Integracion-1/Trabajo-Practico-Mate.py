# EJERCICIO 2 "CONVERSIÓN de NÚMEROS"
# Desarrollar un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
# Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.

# -- Definimos las funciones de conversion. --

# -- Conversion de decimal(base10) a binario(base2) --
def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal //=2
    return binario

# -- Conversion de binario(base2) a decimal(base10). --
def binario_a_decimal(binario):
    decimal = 0
    for posicion, digito in enumerate(reversed(binario)):
        decimal += int(digito) * (2 ** posicion)
    return decimal

# -- Definimos las funciones de validación. --
def validar_decimal(num):
    try:
        num = int(num)
        if num < 0:
            return False, "ERROR. El número ingresado no es admitido."
        return True, num
    except ValueError:
        return False, "ERROR. La entrada no es número decimal valido."


def validar_binario(num):
    if not all(bit in '01' for bit in num):
        return False, "ERROR. El número binario solo debe contener 0 (ceros) y 1 (unos)"
    return True, num

# -- Presentamos al usuario un menú con tres opciones posibles. --
print("---- CONVERSOR DE DECIMAL A BINARIO Y BINARIO A DECIMAL ----")
print("[1]. Convertir Decimal a Binario")
print("[2]. Convertir Binario a Decimal")
print("[3]. Salir")

opcion = input("Seleccione una opcion [1-2-3]: ")

# -- Dependiendo de la Entrada ingresada por el usuario el programa va a analizarla y regresar como salida el resultado esperado por el usuario. --
if opcion == "1":
    num_decimal = input("Ingrese un número decimal a convetir: ")
    num_valido, resultado = validar_decimal(num_decimal)
        
    if num_valido:
        binario = decimal_a_binario(resultado)
        print(f"El número {resultado} convertido a binario es: {binario}")
    else:
        print(resultado)
        
elif opcion == "2":
    num_binario = input("Ingrese un número binario a convertir: ")
    num_valido, resultado = validar_binario(num_binario)
    if num_valido:
        decimal = binario_a_decimal(resultado)
        print(f"El número binario {resultado} convertido a decimal es: {decimal}")
    else:
        print(resultado)
        
elif opcion == "3":
    print("Seleccionó la opcion [SALIR], Gracias! vuelva pronto!")
    exit()
else:
    print("La opcion ingresada no es válida. Por favor, seleccione una opción entre 1, 2 o 3")

# -- FIN DEL PROGRAMA --

# EJEMPLO A UTILIZAR
# numero decimal = 2025
# numero binario = 11111101001
