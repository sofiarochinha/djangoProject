from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomePageView, name="home"),
    path("noticias/", views.Noticias.as_view(), name="noticias"),
    path("inserir-noticia/", views.inserir, name="inserirNoticia"),
    path("filtrar/", views.filtrarNoticia, name="filtrar"),
    path("filtrar-noticia/", views.filtrar, name="filtrarNoticia"),
]