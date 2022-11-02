from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader



def welcome(request):
    return HttpResponse("Hola coders! GATOS")

def login(request):
    return HttpResponse("E AMIGO PASAME EL USUARIO Y LA PASS ;)")

def dia_hoy(request):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy}"
    return HttpResponse(respuesta)

def anio_nacimiento(request, edad):
    
    edad = int(edad)

    anio_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en {anio_nac}")



def vista_plantilla(request):
    # Abrimos el archivo
    archivo = open(r"C:\Users\Mostro\Documents\Python Coderhouse\proyectocoder\templates\plantilla_bonita.html")

    # Creamos el objeto "plantilla"
    plantilla = Template(archivo.read())

    # Cerramos el archivo para liberar recursos
    archivo.close()

    # Diccionario con datos para la plantilla
    datos = {"nombre": "Leonel", "fecha": datetime.now(), "apellido": "Gareis"}

    # Creamos el contexto
    contexto = Context(datos)

    # Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)

    # Retornamos la respuesta
    return HttpResponse(documento)



def vista_listado_alumnos(request):

    # Abrimos el archivo
    archivo = open("C:/Users/Mostro/Documents/Python Coderhouse/proyectocoder/templates/listado_alumnos.html")

    # Creamos el template
    plantilla = Template(archivo.read())

    # Cerramos el archivo para liberar recursos
    archivo.close()

    # Creamos el diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante",  "Barbara Pino"]


    datos = {"tecnologia": "React", "listado_alumnos": listado_alumnos}

    # Creamos el contexto
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def vista_listado_alumnos2(request):
    # Creamos el diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante",  "Barbara Pino"]
    datos = {"tecnologia": "react", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)
