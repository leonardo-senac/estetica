from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('cadastro_servico/', cadastro_servico, name='cadastro_servico'),
    path('servico_dia/', servico_dia, name='servico_dia'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)