from django.contrib import admin
from uapapp.models import Dependencia, Programa, UsuarioDependencia
from django.contrib.auth.models import Permission


admin.site.register(Dependencia)
admin.site.register(Programa)
admin.site.register(UsuarioDependencia)
admin.site.register(Permission)