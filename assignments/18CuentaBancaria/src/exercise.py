def main():
    #escribe tu código abajo de esta línea
    print("BANCO")
    mes = float(input("DAME LO DEL MES PASADO: "))
    ingreso = float(input("DAME LOS INGRESOS: "))
    egresos = float(input("DAME LOS EGRESOS: "))
    cheque = int(input("DAME LOS CHEQUES: "))

    chequet = cheque * 13 
    total1 = mes + ingreso + egresos + chequet 
    total = 7.5/total1
    #Leer los datos
    print("TU TOTAL ES DE:", total)
    pass


if __name__ == '__main__':
    main()
