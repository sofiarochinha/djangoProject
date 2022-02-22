from django.forms import ModelForm
from pages.models import Noticia

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'