import os

isActive = True
while isActive:
    os.system("clear")
    print("Bienvenidos al generador de triangulos de")
    try:
        n=int(input("Ingrese la cantidad de base del triangulo\n Presione 0 si desea salir: "))
        if n==0:
            isActive= False
            print("Gracias por usar el programa")
        elif n > 1:
            for i in range (1, n+1):
                print("*" * i)
            input("presione Enter para continuar")
            
        else:
            print("No existe un triangulo con base 1")
            input("presione Enter para continuar")
            
    except ValueError:
        print("Debe ingresar un numero entero")    
        input("presione Enter para continuar")
