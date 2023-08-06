from django.shortcuts import render, redirect
"""
render=mustra una plantilla HTML junto con los datos proporcionados.
Redirect=se utiliza para redireccionar a otra URL dentro de la aplicación web
 el navegador del usuario será enviado automáticamente a la nueva URL especificada
 """
#-------------------------------------------------------#
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
"""
UserCreationForm=Facilita la creación de nuevos usuarios y se utiliza para registrar nuevos usuarios en la aplicación(Usuario,contraseña,contraseña)
AuthenticationForm= Se utiliza para autenticar a los usuarios existentes"""
#-------------------------------------------------------#
from django.contrib.auth.models import User
"""Se utiliza para manejar la información de los usuarios registrados en una aplicación web Django 
y proporciona funcionalidades relacionadas con la autenticación y autorización de usuarios"""
#-------------------------------------------------------#
from django.db import IntegrityError
"""
Nos ayuda a capturar y manejar errores relacionados con la integridad de la base de datos, 
 especialmente al realizar operaciones de inserción, actualización o eliminación de datos
 """
#-------------------------------------------------------#
from django.contrib.auth import login, logout, authenticate
#Esto  es el sistema de autenticación de Django y se utilizan para facilitar el inicio de sesión y cierre de sesión de usuarios en una aplicación web.
#-------------------------------------------------------#

#Se define home y se llama a la plantilla (template )home.html
def home(request):

    return render(request, 'home.html')

#Creacion de usuario nuevo 
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('EBloque1')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Passwords do not match'
        })


def EBloque1(request):
    return render(request, 'EBloque1.html')

def ejercicios2(request):
    return render(request, 'ejercicios2.html')

def elbloque3(request):
    return render(request, 'elbloque3.html')

def new(request):
    return render(request, 'new.html')
#Se cierra sesión abierta
def signout(request):

    logout(request)
    return redirect('home')

#Se ingresa con un usuario registrado
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
         
         if user is None:
            return render(request, 'signin.html', {
           'form': AuthenticationForm,
           'error': 'Username or password is incorrect'
            })  
         else:
             login(request, user)
             return  redirect('EBloque1')        

def bloque1(request):
    return render(request, 'bloque1.html')

def bloque2(request):
    return render(request, 'bloque2.html')

def bloque1prueba(request):
    return render(request, 'bloque1prueba.html')

def MRU(request):
    return render(request, 'MRU.html')
def MRUV(request):
    return render(request, 'MRUV.html')

def UNI(request):
    return render(request, 'UNI.html')

def sum(request):
    return render(request, 'sum.html')

def cai(request):
    return render(request, 'cai.html')

def ecuah(request):
    return render(request, 'ecuah.html')
def ecuav(request):
    return render(request, 'ecuav.html')

def trabajo(request):
    return render(request, 'trabajo.html')

def energia(request):
    return render(request, 'energia.html')
