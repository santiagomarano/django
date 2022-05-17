from django.http import HttpResponse
from django.template import Template, Context

def saludar(request):

    return HttpResponse("Mi primer mensaje desde Django" + "<h1>HTML<h1>")


def mayor_edad(request, edad):

    if edad >= 18:
        return HttpResponse("Usted es mayor de 18")
    else:
        return HttpResponse("Usted es menor ")


def probando_template(request):

    mi_html = open("/home/san/Escritorio/Nubity/Certificaciones/Python/05-10 - Clase17/proyecto_uno/proyecto_uno/plantillas/web.html")

    plantilla = Template( mi_html.read())

    mi_html.close()

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)