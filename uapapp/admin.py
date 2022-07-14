from django.contrib import admin
from django.contrib.auth.models import Permission

from uapapp.models import Dependencia, Programa, UsuarioDependencia

admin.site.register(Permission)

@admin.register(Programa)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'tipo',)
    list_filter = ('dependencia',)

class ProgramaViewInLine(admin.StackedInline):
    model = Programa
    extra = 1

@admin.register(Dependencia)
class DependenciaAdmin(admin.ModelAdmin):
    inlines = [ProgramaViewInLine,]

@admin.register(UsuarioDependencia)
class UsuarioDependenciaAdmin(admin.ModelAdmin):
    ordering = ('user',)
    list_display = ('user', 'dependencia')
    list_filter = ('user', 'dependencia')
