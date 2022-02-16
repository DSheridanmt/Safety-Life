from django.contrib import admin

#importar classes
from .models import Publicacao, Tag

# Register your models here.

admin.site.register(Publicacao)
admin.site.register(Tag)