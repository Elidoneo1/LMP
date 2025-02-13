def contar_vocales():
    suma = 0
    vocales = "aeiouAEIOU"
    s = input("Ingresa un string: ")
    
    for letter in s:
        if letter in vocales:
            suma += 1
    
    print("Número de Vocales:", suma)

def suma_numeros():
    suma = 0
    num = 1
    
    while num <= 6:
        suma += num
        num += 1
    
    print("Suma de los números del 1 al 6:", suma)

def main():
    while True:
        opcion = input("Presiona 1 para contar vocales, 2 para sumar números o 3 para salir: ")
        
        if opcion == "1":
            contar_vocales()
        elif opcion == "2":
            suma_numeros()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
