from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    context = {
        'título': 'Armário de chaves do',
        'Nome': 'Matheus Lucas',
    }
    return render(request, 'index.html', context)

def status_api(request):
    # O armario precisa saber se o servidor está acordado
    return JsonResponse({'status': 'online', 'sistema': 'key_track IoT'})