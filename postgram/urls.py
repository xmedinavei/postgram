"""postgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


    postgram URLs module.
"""
#Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

#'PATH(url)', VISTA.FUNCION_A_REALIZAR (mirar alias en import), 'ALIAS DE URL'
urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')), #1ro: ubicacion del archivo url.py. 2do: a que app pertenece.

    path('users/', include(('users.urls', 'users'), namespace='users')), #1ro: ubicacion del archivo url.py. 2do: a que app pertenece.

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #lo ultimo para mostrar imagenes #ver settings.py MEDIA_ROOT y MEDIA_URL
