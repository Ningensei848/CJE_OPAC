
from django.views.generic.base import TemplateView

from opac.forms.search import SearchForm


class IndexView(TemplateView):

    template_name = 'opac/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = SearchForm

        return context
