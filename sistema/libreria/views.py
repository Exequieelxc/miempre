from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmprendimientoForm
from .models import Emprendimiento

def inicio(request):
    return render(request, 'paginas/inicio.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

def explorar(request):
    emprendimientos = Emprendimiento.objects.all()
    return render(request, 'paginas/explorar.html', {'emprendimientos': emprendimientos})

def planes_y_precios(request):
    return render(request, 'paginas/planes_y_precios.html')

def acerca_de_nosotros(request):
    return render(request, 'paginas/acerca_de_nosotros.html')

def registro(request):
    return render(request, 'paginas/registro.html')

def registrar_emprendedor(request):
    return render(request, 'paginas/registro_exitoso.html')

def registrar_empresa_grande(request):
    return render(request, 'paginas/registro_exitoso.html')

def registrar_emprendimiento(request):
    if request.method == 'POST':
        formulario = EmprendimientoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('explorar')  # Redirige a donde sea apropiado después de registrar el emprendimiento
    else:
        formulario = EmprendimientoForm()

    return render(request, 'paginas/registrar_emprendimiento.html', {'formulario': formulario})