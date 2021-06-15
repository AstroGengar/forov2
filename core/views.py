from django.shortcuts import render, redirect
from .models import Anime
from .forms import AnimeForms, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def manga(request):
    return render(request, 'core/manga.html')

def anime(request):
    return render(request, 'core/anime.html')

def sobrenosotros(request):
    return render(request, 'core/sobrenosotros.html')

def blackclover(request):
    return render(request, 'core/blackclover.html')

def maou(request):
    return render(request, 'core/maou.html')

def naruto(request):
    return render(request, 'core/naruto.html')

def onepiece(request):
    return render(request, 'core/onepiece.html')

def shingeki(request):
    return render(request, 'core/shingeki.html')

def list_anime(request):
    return render(request, 'core/list_anime.html')

#listar
def listado_anime(request):
    anime = Anime.objects.all()
    data = {
        'anime':anime
    }
    return render(request, 'core/listado_anime.html', data)

#agregar
@permission_required('core.add_anime')
def nuevo_anime(request):
    data = {
        'form':AnimeForms()
    }
    if request.method == 'POST':
        formulario = AnimeForms(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado con éxito"
        data['form'] = formulario

    return render(request, 'core/nuevo_anime.html', data)

#modificar
@permission_required('core.change_anime')
def modificar_anime(request, id):
    anime = Anime.objects.get(id=id)
    data = {
        'form':AnimeForms(instance=anime)
    }

    if request.method == 'POST':
        formulario = AnimeForms(data=request.POST, instance=anime, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificación con éxito"
        data['form'] = AnimeForms(instance=Anime.objects.get(id=id))

    return render(request, 'core/modificar_anime.html', data)

#eliminar
@permission_required('core.delete_anime')
def eliminar_anime(request, id):
    anime = Anime.objects.get(id=id)
    anime.delete()

    return  redirect(to="listado_anime")

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #Autenticar al usuario para redirigirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/registrarse.html', data)
