repeticiones = int(input("Ingrese la cantidad de veces que quiere usar la calculadora: "))

for i in range(repeticiones):
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    resultado = None
    operacion = input("Ingrese la operación que desea realizar: ")
    
    if operacion == "+":
        resultado = num1 + num2
    
    elif operacion == "-":
        resultado = num1 - num2
    
    elif operacion == "*":
        resultado = num1 * num2
    
    elif operacion == "/":
        resultado = num1 / num2
    else:
        print("Operación no válida")
    if resultado is not None:
        print(f"El resultado de la operación es: {resultado}")