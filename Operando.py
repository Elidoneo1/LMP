from clase_Calc import  Calculadora

print("\nCalculadora")
print ("\nPara salir presione s")
print("Operacion:")


while True:
    expresion = input("\n ")
    if expresion.lower() == "s":
        print("\nAdios...")
        break
    else:
        print(Calculadora.operando(expresion))
        

    

    
