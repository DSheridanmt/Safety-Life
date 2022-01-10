from django.contrib import admin

#importar classes
from .models import Admin, Publicacao, Tag

# Register your models here.
admin.site.register(Admin)
admin.site.register(Publicacao)
admin.site.register(Tag)