from django.urls import path, include
from .views import home, manga, anime, sobrenosotros, blackclover, maou, naruto, onepiece, shingeki, list_anime, listado_anime, nuevo_anime, modificar_anime, eliminar_anime, registro_usuario, AnimeViewSet

#Permitimos crear las URLs necesarias para nuestra API
from rest_framework import routers

router = routers.DefaultRouter()
#Todas estas rutas que genera "routers" se registran en el path
router.register('anime', AnimeViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('manga/', manga, name="manga"),
    path('anime/', anime, name="anime"),
    path('sobrenosotros/', sobrenosotros, name="sobrenosotros"),
    path('blackclover/', blackclover, name="blackclover"),
    path('maou/', maou, name="maou"),
    path('naruto/', naruto, name="naruto"),
    path('onepiece/', onepiece, name="onepiece"),
    path('shingeki/', shingeki, name="shingeki"),
    path('list-anime', list_anime, name="list_anime"), 
    path('listado-anime/', listado_anime, name="listado_anime"),
    path('nuevo-anime/', nuevo_anime, name="nuevo_anime"),
    path('modificar-anime/<id>/', modificar_anime, name="modificar_anime"),
    path('eliminar-anime/<id>/', eliminar_anime, name="eliminar_anime"),
    path('registro/', registro_usuario, name="registro_usuario"),
    #El routers nos generarĂ¡ todas las urls como el CRUD y son pasadas a django con el prefijo API
    path('api/', include(router.urls)),
]