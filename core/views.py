from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .utils import buscar_status_nichos_banco


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
        dados_nichos = dictfetchall(cursor)

    # 3. Resposta
    return JsonResponse({'nichos': dados_nichos}, safe=False)


def api_status_nichos(request):

    nichos = buscar_status_nichos_banco()
    return JsonResponse(nichos, safe=False, status=200)
