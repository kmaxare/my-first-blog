from django.urls import path
from . import views

#path('url_concreta', ubicacion_deVista, str_reemplazo_de_url)

urlpatterns = [
    path('', views.post_list, name='post_list'),
]