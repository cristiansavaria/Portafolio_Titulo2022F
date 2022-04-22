from django.shortcuts import render

# Create your views here.se crea primero la vista luego se agrega la urls en e l modulo
def base(request):
    return render(request, 'app/base.html')
def servicio(request):
    return render(request, 'app/servicios.html')
def reserva_hora(request):
    return render(request, 'app/reserva_hora.html')
def contacto(request):
    return render(request, 'app/contacto.html')
def quienes_somos(request):
    return render(request, 'app/quienes_somos.html')


def login(request):
    return render(request, 'app/login.html')
def registro(request):
    return render(request, 'app/registro.html')

def error404(request):
    return render(request, 'app/error404.html')