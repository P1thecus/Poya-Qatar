
#! * * * * * * PRELIMINARES * * * * * * * * * * * * * * * * * * * * * * * * * * * *



#! * * * * * * FUNCIONAMIENTO * * * * * * * * * * * * * * * * * * * * * * * * * * *


#todo+ + + + + MENU + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +


#? - - - - - - DEFINICIÓN DE LA ACCION DEL MENÚ A EJECUTAR - - - - - - - - - - - - -

#--------------nivel 1 del menú
print("\nMENU")
print("\n--ADMINISTRADOR (1)\n--APOSTADOR (2)\n")
opcion_1 = input("Ingresa opción: ")

#--------------nivel 2 del menú
if opcion_1 == "1":
    print("\n--DEFINIR INSTRUCCIONES (1)\n--ADMINISTRAR GRUPOS Y USUARIOS (2)\n--REGISTRAR RESULTADOS (3)\n")
elif opcion_1 == "2":
    print("\n--PRONOSTICAR (1)\n--CONSULTAR (2)\n--SER ALERTADO (3)\n")

opcion_2 = input("Ingresa opción: ")
if opcion_1 == "1" and opcion_2 == "1":
    accion = "definir instrucciones"
elif opcion_1 == "1" and opcion_2 == "2":
    accion = "administrar grupos y usuarios"
elif opcion_1 == "1" and opcion_2 == "3":
    accion = "registrar resultados"
elif opcion_1 == "2" and opcion_2 == "1":
    accion = "pronosticar"
elif opcion_1 == "2" and opcion_2 == "2":
    accion = "consultar"
elif opcion_1 == "2" and opcion_2 == "3":
    accion = "ser alertado"

print("\n",accion,"\n")

