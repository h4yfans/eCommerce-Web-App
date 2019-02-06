from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm
from django.contrib.auth import authenticate, login


def home_page(request):
    context = {
        "title": "Hello world!",
        'content': 'welcome to homeage',
        'premium_content' : 'yeah!'
    }
    return render(request, 'home_page.html', {})


def about_page(request):
    return render(request, 'home_page.html', {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "context": "Welcome to contact page",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'home_page.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)

        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            context['form'] = LoginForm()
            return redirect('/login')
        else:
            print('Error')

    return render(request, 'auth/login.html', context)


def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'auth/register.html', {})
