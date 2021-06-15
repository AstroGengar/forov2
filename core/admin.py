from django.contrib import admin
from .models import Genero, Anime
# Register your models here.

class AnimeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'capitulos', 'temporadas', 'genero']
    #search_fields = ['nombre', 'genero']
    list_filter = ['genero']
    list_per_page = 10


admin.site.register(Genero)
admin.site.register(Anime, AnimeAdmin)