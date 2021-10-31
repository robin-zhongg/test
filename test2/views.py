from django.shortcuts import render


def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)


def index2(request):
    context = {}
    context['hello'] = 'Hello2 World!'
    return render(request, 'index.html', context)

