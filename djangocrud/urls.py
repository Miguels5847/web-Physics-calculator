"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
    
"""
#-------------------------------#
from django.contrib import admin
"""Esto permite gestionar los datos de la base de datos y administrar ciertos aspectos de la aplicación web sin tener que 
escribir código personalizado para cada operación de administración."""
#-------------------------------#
from django.urls import path
# se utiliza para definir rutas (URLs) en el sistema de enrutamiento de la aplicación web.
#-------------------------------#
import pip
"""
import pip te permitía acceder a la funcionalidad del paquete pip, como instalar, desinstalar o listar paquetes.
"""
#-------------------------------#
from primerb import views
#Se importa de la Carpeta primerb el .py que es las views en donde se realizo las diferentes funciones
#-------------------------------#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('EBloque1/',views.EBloque1, name='EBloque1'),
    path('elbloque3/',views.elbloque3, name='elbloque3'),
    path('MRU/',views.MRU, name='MRU'),
    path('MRUV/',views.MRUV, name='MRUV'),
    path('UNI/',views.UNI, name='UNI'),
    path('sum/',views.sum, name='sum'),
    path('cai/',views.cai, name='cai'),
    path('ecuah/',views.ecuah, name='ecuah'),   
    path('ecuav/',views.ecuav, name='ecuav'), 
    path('trabajo/',views.trabajo, name='trabajo'),
    path('energia/',views.energia, name='energia'),    
    path('ejercicios2/',views.ejercicios2, name='ejercicios2'),
    path('new/',views.new, name='new'),    
    path('bloque1/',views.bloque1, name='bloque1'),
    path('bloque2/',views.bloque2, name='bloque2'),
    path('bloque1prueba/',views.bloque1prueba, name='bloque1prueba'),
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin, name='signin')
]
