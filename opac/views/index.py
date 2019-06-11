
from django.views.generic.base import TemplateView
from opac.models.bibliography import BIBLIO


class IndexView(TemplateView):

    template_name = 'opac/index.html'
