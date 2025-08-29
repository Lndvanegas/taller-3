import os

plata=100000

os.system("clear")

isActive=True

while True:
    print("1. consultar saldo")
    print("2. depositar dinero")
    print("3. retirar dinero")
    print("0. salir")


    option = int(input("Ingresa una de las 4 opciones: "))

    match option:
        
        case 1:
                                os.system("clear")
                                print(f"su saldo es:{plata} ")
                                input("presiona ↵ para continuar")
                                os.system("clear")

        case 2:
                                os.system("clear")
                                deposito=int(input("ingrese el valor a depositar: "))
                                plata+=deposito
                                print(f"Su nuevo saldo es: {plata}")
                                input("presiona ↵ para continuar")
                                os.system("clear")
        case 3:
            os.system("clear")
            negativo=int(input("ingrese el valor a retirar: "))
            plata-=negativo
            print(f"Su nuevo valor es: {plata}")
            input("presione ↵ para continuar")
            s.system("clear")




                                


                                

