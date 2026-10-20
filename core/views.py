from django.shortcuts import render


def index(request):
    context = {
        'título': 'Armário de chaves do',
        'Nome': 'Matheus Lucas',
    }
    return render(request, 'index.html', context)
