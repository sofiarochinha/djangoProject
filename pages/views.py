from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.views.generic import TemplateView

#inserir noticia
from .forms import NoticiaForm
from pages.models import Noticia


def HomePageView(request):
    noticias = Noticia.objects.all()
    return render(request, "noticias.html", { 'noticias': noticias })


class Noticias(TemplateView):
    template_name = "noticias.html"

#insere a noticia na base de dados
def inserir(request):
    form = NoticiaForm()

    if(request.method == 'POST'):
        form = NoticiaForm(request.POST)

        if(form.is_valid()):
            form.save()


    context = {'form': form}
    return render(request, 'inserirNoticia.html', context)


def filtrarNoticia(request):
    if request.POST:
        tag = request.POST['selected_tag']
        noticias = Noticia.objects.all()
        list = []

        for noticia in noticias:
            if noticia.tag == tag:
                list.append(noticia)

        context = {'list': list, 'noticias': noticias}
        return render(request, 'filtrarNoticia.html', context)


def filtrar(request):
    noticias = Noticia.objects.all()
    return render(request, "filtrarNoticia.html", {'noticias': noticias})