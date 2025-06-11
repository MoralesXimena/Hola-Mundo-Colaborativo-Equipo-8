class Saludo:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar_saludo(self):
        print(self.mensaje)


if __name__ == "__main__":
    saludo = Saludo("Hola Mundo")
    saludo.mostrar_saludo()
