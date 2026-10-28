"""
URL configuration for key_track project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: jafrom dngo.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# core/utils.py
from django.db import connection


def dictfetchall(cursor):
    """Converte todas as linhas de um cursor em uma lista de dicionarios."""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def buscar_status_nicho_banco():
    """Consulta a View SQL vw_status_nicho hospedada no Supabase."""
    query = "SELECT * FROM vw_status_nicho ORDER BY nicho_id ASC;"

    with connection.cursor() as cursor:
        cursor.execute(query)
        dados = dictfetchall(cursor)

    return dados
