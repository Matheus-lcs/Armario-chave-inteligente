from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .utils import buscar_status_nicho_banco


def dictfetchall(cursor):
    """Converte o resultado do cursor em uma lista de dicionários."""
    colunas = [col[0] for col in cursor.description]
    return [dict(zip(colunas, linha)) for linha in cursor.fetchall()]


def index(request):
    context = {
        'titulo': 'Armário de chaves do',  # complete o texto, parece cortado
        'nome': 'Matheus Lucas',
    }
    return render(request, 'index.html', context)


def status_api(request):
    # O armário precisa saber se o servidor está acordado
    return JsonResponse({'status': 'online', 'sistema': 'key_track IoT'})


def status_nicho_view(request):
    # 1. Conexão e execução
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM vw_status_nichoview")

        # 2. Transformação
        dados_nicho = dictfetchall(cursor)

    # 3. Resposta
    return JsonResponse({'nicho': dados_nicho}, safe=False)


def api_status_nicho(request):

    nicho = buscar_status_nicho_banco()
    return JsonResponse(nicho, safe=False, status=200)
