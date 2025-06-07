from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from empleados.models import Empleado

def landing_page(resquest):
    empleados = Empleado.objects.all()
    return render(resquest, 'landing/landing_page.html', {
        'empleados': empleados
    })