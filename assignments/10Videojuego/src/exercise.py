def main():
    #escribe tu código abajo de esta línea
    print("VIDEOJUEGO")
    nuevo = int(input("DAME LOS NUEVOS: "))
    usado = int(input("DAME LOS USADOS: "))
    total = (nuevo * 1000) + (usado * 350)
    #Leer los datos
    print("TU TOTAL ES DE:", total)
    pass


if __name__ == '__main__':
    main()
