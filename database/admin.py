from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin

# Departamentos

class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('nombre',)
    
    # Campos visibles en admin
    list_display = ('nombre',)

admin.site.register(Departamento, DepartamentoAdmin)

# Computadores y Laptops

class EmpleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('nombre', 'cedula')
    
    # Campos visibles en admin
    list_display = ('nombre', 'departamento', 'cargo', 'cedula')
    
    # Campos filtrables en admin
    list_filter = ('departamento', 'cargo')

admin.site.register(Empleado, EmpleadoAdmin)
def equipo_no_operativo(modeladmin, request, queryset):
    for obj in queryset:
        # Create a new SourceModel object with the same dat
        
        if (hasattr(obj, 'usuario')):
            
            source_obj = Desincorporacion.objects.create(
            bien_nacional=obj.bien_nacional,
            usuario=obj.usuario,
            marca=obj.marca,
            modelo=obj.modelo
            )
        else:   
            
            source_obj = Desincorporacion.objects.create(
            bien_nacional=obj.bien_nacional,
            usuario= None,
            marca=obj.marca,
            modelo=obj.modelo
            )
            
        # Delete the TargetModel object
        obj.delete()

equipo_no_operativo.short_description = "Marcar como activo no operativo"

def equipo_en_solvencia(modeladmin, request, queryset):
    for obj in queryset:
        # Create a new SourceModel object with the same dat
        
        if (hasattr(obj, 'usuario')):
            
            source_obj = Solvencia.objects.create(
            bien_nacional=obj.bien_nacional,
            usuario=obj.usuario,
            marca=obj.marca,
            modelo=obj.modelo
            )
        else:   
            
            source_obj = Solvencia.objects.create(
            bien_nacional=obj.bien_nacional,
            usuario= None,
            marca=obj.marca,
            modelo=obj.modelo
            )
            
        # Delete the TargetModel object
        obj.delete()

equipo_en_solvencia.short_description = "Marcar como activo en solvencia"

class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia]

    # Campos buscables en admin
    search_fields = ('usuario__nombre',)
    
    # Campos visibles en admin
    list_display = ('usuario', 'procesador', 'ram', 'almacenamiento', 'tipo_disco', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('usuario__departamento', 'usuario__cargo')

admin.site.register(Equipo, EquipoAdmin)

class ImpresoraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia]

    # Campos buscables en admin
    search_fields = ('marca', 'modelo')
    
    # Campos visibles en admin
    list_display = ('marca', 'modelo', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('marca',)

admin.site.register(Impresora, ImpresoraAdmin)

class TelefonoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia]

    # Campos buscables en admin
    search_fields = ('usuario__nombre', 'numero')
    
    # Campos visibles en admin
    list_display = ('usuario', 'numero', 'marca', 'modelo', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('usuario__departamento', 'usuario__cargo',)

admin.site.register(Telefono, TelefonoAdmin)

class SwitchAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia]

    # Campos buscables en admin
    search_fields = ('marca', 'modelo')
    
    # Campos visibles en admin
    list_display = ('marca', 'modelo', 'puertos', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('marca',)

admin.site.register(Switch, SwitchAdmin)

class RouterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia]
    
    # Campos buscables en admin
    search_fields = ('marca', 'modelo')
    
    # Campos visibles en admin
    list_display = ('marca', 'modelo', 'puertos', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('marca',)

admin.site.register(Router, RouterAdmin)

class DesincorporacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    # Campos visibles en admin
    list_display = ('bien_nacional', 'usuario', 'marca', 'modelo')
    
    # Campos buscables en admin
    
    search_fields = ('modelo',)    
    # Campos filtrables en admin
    
admin.site.register(Desincorporacion, DesincorporacionAdmin)

class SolvenciaAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    # Campos visibles en admin
    list_display = ('bien_nacional', 'usuario', 'marca', 'modelo')
    
    # Campos buscables en admin
    
    search_fields = ('modelo',)    
    # Campos filtrables en admin
    
    # Campos filtrables en admin
    
admin.site.register(Solvencia, SolvenciaAdmin)

