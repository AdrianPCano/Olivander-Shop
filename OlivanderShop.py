def accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero):

    """
    : matrizCasosTest: Rescibe una matriz vacía.
    : rutaAccesoFichero: Indica la ruta del fichero que se va a leer.
    : return: Devuelve una lista vacía con un mensaje advertiendo del problema.
    Si todo es correcto la función devuelve una matriz con los objetos que hay en los casos test, en este caso los objetos de la tienda, separados por coma.

    """

    try:
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        print("Fichero no encontrado")
        return []
    except ValueError:
        print("El nombre del fichero ha de ser un string")
        return []
    else:
        matrizCasosTest = []
        numeroPropiedadesItem = 0
        for linea in fichero:
            if linea.find("day") != -1:
                casosTestDia = []
            elif linea == "\n":
                matrizCasosTest.append(casosTestDia)
            elif linea.find("name") != -1:
                numeroPropiedadesItem = len(linea.split(','))
            else:

                #No cumple con lo que nos piden, se tiene que refactorizar.
                
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem - 1)
                casosTestDia.append(item)
        fichero.close()
        return matrizCasosTest


def crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest):

    """
    : ficheroVolcadoCasosTest: Se crea un fichero con la información de los objetos de la tienda.
    : matrizCasosTest: Es una matriz que contiene los datos del fichero que forman los casos test.
    : return: En este caso no devuelve nada, crea un fichero .gr con los objetos de la tienda transformados.
    """
    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
            print("La ruta de acceso al fichero ha de ser un string")
    else:
        for (offset, casosTestDia) in enumerate(matrizCasosTest):
            stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
            for item in casosTestDia:
                stdout.write(','.join(item) + '\n')
        stdout.close()


def mostrarCasosTest(matrizCasosTest):

    """
    : matrizCasosTest: Matriz con los elementos de la tienda separados por ','.
    : return: En este caso no devuelve nada, imprime por pantalla los objetos de la tienda en forma de lista.

    """

    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)


if __name__ == "__main__":

    rutaAccesoFichero = "./stdout.gr"
    # rutaAccesoFichero = "stdout_bug_conjured.g"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    mostrarCasosTest(matrizCasosTest)

    ficheroVolcadoCasosTest = "./stdout.txt"

    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)