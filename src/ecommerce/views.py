from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        "title" : "He"
    }
    return render(request, 'home_page.html', {})

def about_page(request):
    return render(request, 'home_page.html', {})

def contact_page(request):
    return render(request, 'home_page.html', {})
