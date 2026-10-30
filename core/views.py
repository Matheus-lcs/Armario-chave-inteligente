
from django.shortcuts import render
from django.http import JsonResponse
from .utils import buscar_status_nicho_banco


def index(request):
    context = {
        'titulo': 'Armário de chaves',
        'nome': 'Matheus Lucas',
    }
    return render(request, 'index.html', context)


def status_api(request):
    return JsonResponse({
        'status': 'online',
        'sistema': 'key_track IoT',
    })


def status_nicho_view(request):
    try:
        dados_nicho = buscar_status_nicho_banco()
        return JsonResponse({'nicho': dados_nicho})

    except Exception as erro:
        return JsonResponse(
            {'erro': str(erro)},
            status=500,
        )


def api_status_nicho(request):
    try:
        nicho = buscar_status_nicho_banco()
        return JsonResponse(nicho, safe=False, status=200)

    except Exception as erro:
        return JsonResponse(
            {'erro': str(erro)},
            status=500,
        )
