import random
import pycountry
from time import sleep
from colorama import init, Fore, Back, Style
init(autoreset=True)
def nombre_pais(consulta):
    try:
        pais = pycountry.countries.search_fuzzy(consulta)[0]
        return pais.name
    except LookupError:
        return "País no encontrado."
def login(usuario, contraseña):
    login = open("login.txt")
    for lineas in login.readlines():
        if usuario == lineas.rstrip().split(",")[0] and contraseña == lineas.rstrip().split(",")[1]:
            xxx = True
            break
        else:
            xxx = False
    return xxx
def launch(pais):
    xx = random.randint(1,2)
    print("Buscando Pais...")
    sleep(2)
    try:
        pycountry.countries.search_fuzzy(pais)
    except LookupError:
        print(Fore.RED+"Pais no encontrado")
        return
    country = nombre_pais(pais)

    print("Pais " + country + " Encontrado")
    confirmacion = input("Estas seguro que quieres atacar a " + country + "? Y/N: ")
    confirm = confirmacion.upper()
    sleep(1)
    if confirm == "Y":
        if xx == 1:
            print(Fore.GREEN+"Lanzamiento exitoso")
            sleep(1)
            print(Fore.MAGENTA+Style.BRIGHT+"Felicidades acabas de empezar una guerra contra " + country)
            return
        else:
            print(Fore.RED+Style.BRIGHT+"Fallo en el lanzamiento")
            for arch in ["ABORTANDO EN", "3", "2", "1"]:
                sleep(1)
                print(Fore.RED+Style.BRIGHT+str(arch))
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"ABORTACION COMPLETA")
            return
    elif confirmacion == "N":
        print("Cancelando Procedimiento")
        print("Cancelación Completa")
        return
    else:
        print("Opción Errónea")
        return
def test():
    xx = random.randint(1, 4)
    print("Iniciando Prueba")
    for arch in ["0", "10", "20", "30", "40", "50", "60", "70", "80", "90"]:
        sleep(2)
        print(Fore.YELLOW + str(arch+"%"))
    if xx == 1:
        print(Fore.YELLOW+"100%")
        print(Fore.GREEN+Style.BRIGHT+"Prueba finalizada con exito")
        return
    else:
        for alv in ["HA OCURRIDO UN ERROR CATASTROFICO", "INICIANDO PROTOCOLO DE LANZAMIENTO DE LOS MISILES NUCLEARES", "BUSCANDO OBJETIVO", "OBJETIVO ENCONTRADO", "INICIANDO LANZAMIENTO HACIA KARJISTÁN", "LOS MISILES LLEGARAN A SU DESTINO EN 30 SEGUNDOS"]:
            sleep(2)
            print(Fore.RED+Style.BRIGHT+str(alv))
        exit("CONEXION CON EL SERVIDOR INTERRUMPIDA ")
def help():
    print("Los comandos que puedes utilizar son los siguientes:")
    print("lanzar: Inicia el protocolo de lanzamiento de misiles hacia el pais designado")
    print("probar: Inicia las pruebas del sistema para ver si todo esta en orden")
    print("salir: Cierra la sesión del usuario al que estes conectado y finaliza el programa ")
def abort():
    print("Cerrando sesión")
    sleep(1)
    print("Sesión cerrada")
    sleep(1)
    exit()
def commands(coman):
    comando = coman
    if comando == "lanzar":
        country = input("Ingresa el país a Atacar: ")
        launch(country)
    elif comando == "probar":
        test()
    elif comando == "ayuda":
        help()
    elif comando == "salir":
        abort()
    else:
        print("Comando invalido")

user = input("Ingresa el usuario: ")
password = input("Ingresa la contraseña: ")

if login(user, password) == True:
    print("Bienvenido Programador")
else:
    print("Usuario Incorrecto")
    exit()
print("\nEjecute el comando 'ayuda' para saber que hacer.\n")
while True:
    comando = input("Ejecute el Comando que deseé: ")
    commands(comando)