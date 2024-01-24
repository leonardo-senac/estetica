from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('cadastro_servico/', cadastro_servico, name='cadastro_servico'),
    path('servico_dia/', servico_dia, name='servico_dia'),
    path('regulamento/', regulamento, name='regulamento'),
    path('pagina_servico/', pagina_servico, name='pagina_servico'),
    path('local/', local, name='local'),
    path('listagem/', listagem, name='listagem')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)