from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.exceptions import ValidationError


def register(request):
    if request.method == 'GET':
        return render(request,'cadastro/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get(MinimumLengthValidator,'password')
        senha2 = request.POST.get('password2')
        user = User.objects.filter(username=username).first()
        email_banco = User.objects.filter(email=email).exists()


        if user:
            messages.error(request, 'Usuário já Cadastrado!')
            return redirect('login')
        
        if email_banco:
            messages.error(request, 'Email já Cadastrado!')
            return redirect('register')

        if senha2 == senha:
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()

        else:
            messages.error(request, 'As senhas diferem!')
            return redirect('register')
        
        messages.success(request, 'Usuário Cadastrado com Sucesso')
        return redirect('login')




@login_required(login_url='/login/')
def plataforma(request):
    return render(request, 'cadastro/plataforma.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'cadastro/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user:
            login_django(request, user)
            return redirect('plataforma')            
            
        else:
            messages.error(request, 'Usuário ou Senha Inválidos!')
            return redirect('login')

def recuperacao(request):
    if request.method=='GET':
        return render(request, 'cadastro/recuperacao.html')
    else:
        email = request.POST.get('email')
        email_banco = User.objects.filter(email=email).exists()

    if email_banco:
        send_mail("Assunto", "Mensagem Foda.", "tellurisvita@gmail.com", ["gabrielmendonca404@gmail.com"])
        messages.success(request, 'Email Enviado!')
        return redirect('reset_password_done')
        
    else:
        messages.error(request, 'Email não Cadastrado!')
        return redirect('recuperacao')
        


def reset_password(request,):
    if request.method == 'GET':
        return render(request, 'cadastro/reset_password.html')
    else:
        pass
