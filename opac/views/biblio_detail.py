from django.views.generic import DetailView

from opac.models.bibliography import BIBLIO


class BiblioDetailView(DetailView):
    model = BIBLIO  # Equal ==> "queryset = Metadata.objects.all()"
    template_name = 'opac/biblio_detail.html'
    slug_field = 'nbc'
    slug_url_kwarg = 'nbc'
