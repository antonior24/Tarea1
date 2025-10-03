from django.contrib import admin
from .models import Post
from .models import Animal, Protectora, Colaborador
# Register your models here.

admin.site.register(Post)
admin.site.register(Animal)
admin.site.register(Protectora)
admin.site.register(Colaborador)