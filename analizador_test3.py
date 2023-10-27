import re

def caracter(character):
    global simbolo
    simbolo=""
    global eof
    eof=";"
    digito="[0-9]"
    signo="-"
    decimal="\."
    identificador="[a-zA-Z][a-zA-Z0-9]*"
    operador="[+-/*]"
    asignacion="="
    blanco="\s"
    
    #comparamos si es digito o operador
    if(re.match(signo,character)):
        print("entra a signo")
        simbolo="Signo"
        return 0
    else:
        if(re.match(digito,character)):
            simbolo="Digito"
            return 1
        else: 
            if(re.match(decimal,character)):
                simbolo="Decimal"
                return 2
            else:
                if(re.match(identificador,character)):
                    simbolo="Identificador"
                    return 3
                else:
                    if(re.match(operador,character)):
                        simbolo="Operador"
                        return 4
                    else:
                        if(re.match(asignacion,character)):
                            simbolo="Asignacion"
                            return 5
                        else:
                            if(re.match(blanco,character)):
                                simbolo="Blanco"
                                return 6
                            else:
                                if(character==eof):
                                    return 7

def encabezado_tablas():
    print("+------------------+-------------------------+")
    print("|    Símbolos     |         Tipo de Dato     |")
    print("+------------------+-------------------------+")

# Tablas para los símbolos y errores
tabla_simbolos = []
tabla_errores = []
linea_actual = 1
# Tabla de transiciones
tabla=[[1,2,"E",6,8,7,"B","F"],
       ["E",2,"E","E","E","E","B","F"],
       ["E",2,3,"E","E","E","B","F"],
       ["E",4,"E","E","E","E","B","F"],
       ["E",4,"E","E","E","E","B","F"],
       ["E",6,"E",6,"E","E","B","F"],
       ["E","E","E","E","E","E","B","F"],
       ["E","E","E","E","E","E","B","F"],
       ["E","E","E","E","E","E","B","F"],
       ["E","E","E","E","E","E","B","F"]]
estado = 0
almacen = []

print("+-------------------------------------+")
print("|    Ingrese una cadena a evaluar:    |")
print("+-------------------------------------+")
cadena = input()

for character in cadena:
    estadosig = estado
    charcaracter = caracter(character)
    estado = tabla[estado][charcaracter]

    if character == ";":
        linea_actual += 1

    if estado == "E":
        almacen.append(character)
        tabla_errores.append({"Línea": linea_actual, "Cadena": ''.join(almacen)})
        almacen = []
        estado = 0
    else:
        almacen.append(character)

    if estado == "B" and estadosig in [2, 4, 6, 7, 8]:
        tipo = ""
        if estado == 2:
            tipo = "Numero"
        elif estado == 4:
            tipo = "Numero"
        elif estado == 6:
            tipo = "Identificador"
        elif estado == 7:
            tipo = "Asignacion"
        elif estado == 8:
            tipo = "Operador"
        tabla_simbolos.append({"Línea": linea_actual, "Símbolo": ''.join(almacen), "Tipo de Dato": tipo})
        almacen = []
        estado = 0
    elif estado == "B":
        tabla_errores.append({"Línea": linea_actual, "Cadena": ''.join(almacen)})
        almacen = []
        estado = 0

# Imprimimos las tablas al final
print("+--------------------- Tabla de Símbolos ----------------------+")
encabezado_tablas()
for simbolo in tabla_simbolos:
    print(f"| {simbolo['Símbolo']} | {simbolo['Tipo de Dato']} |")

print("+---------------------- Tabla de Errores ----------------------+")
encabezado_tablas()
for error in tabla_errores:
    for key, value in error.items():
        print(f"| {key} | {value} |")