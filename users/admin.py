"""User admin classes."""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.
#admin.site.register(Profile)## #SE REGISTRA EL MODELO DESDE EL MODELS.PY DE ESTA APP

@admin.register(Profile) #Decorador para registro y le mandamos el perfil #VER DOCUMENTACION MODELADMIN
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    
    list_display = ( #para escoger campos a mostrar en el user
        'pk',
        'user',
        'phone_number',
        'website',
        'picture'
        )

    list_display_links = ('pk','user') #para que los items sean clickeables y nos lleven al detalle del user
    list_editable = ('phone_number','website','picture') #campos que se pueden editar directamente

    search_fields = ( #para buscar. User es una relacion, no un objeto (por eso __)
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
        )

    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff') #anadir filtros de busqueda

    fieldsets = ( #al clickear el user, anade opciones. Documentacion en ADMIN
        ('Profile', {
            'fields':(('user', 'picture'),),
            }
        ),
        ('Extra info', {
            'fields': (
                    ('website', 'phone_number'),
                    ('biography')
                )
            }
        ),
        ('Metadata', { #readonly_fields
                'fields':(('created', 'modified'))
            }

        )
    )

    readonly_fields = ('created', 'modified') #si no s epoen esto. El metadata da error porque creatred y modified no es editable, solo para ver.

#para no tener que crear un user y luego un perfil. Hacerlo en un solo paso dentro de user. 
#Documentación de Customizing Authetication
class ProfileInLine(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

#para no tener que crear un user y luego un perfil. Hacerlo en un solo paso dentro de user. 
#Siguendo documentación de Customizing Authetication
class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

#para no tener que crear un user y luego un perfil. Hacerlo en un solo paso dentro de user. 
#Re-registrar UserAdmin. 
#Siguiendo documentacion.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)