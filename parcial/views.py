from django.shortcuts import render

# Create your views here.

def menu_vista(request):
    opciones = ['Reservas', 'Personal', 'Inventario', 'Platos']
    return render(request, 'menu.html', {'opciones': opciones})
