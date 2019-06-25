from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def registrar_usuario(request, template_name='registrar.html'):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        tipo = request.POST['tipo_usuario']
        if tipo == 'administrador':
            user = User.objects.create_user(username, email, password)
            user.is_staff = True
            user.save()
        else:
            user = User.objects.create_user(username, email, password)

        return redirect('')

    return render(request, template_name, {})