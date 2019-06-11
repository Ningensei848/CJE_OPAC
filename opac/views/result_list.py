from django.db.models import Q
from django.views.generic import ListView

from opac.models.bibliography import BIBLIO


class ResultListView(ListView):
    template_name = 'opac/result_list.html'
    model = BIBLIO
    paginate_by = 20  # if pagination is desired
    biblio = BIBLIO.objects.all()

    def get_queryset(self):
        queries = self.request.GET['search']
        biblio = self.biblio
        query = Q()

        for word in queries.split():
            query |= Q(title__icontains=word) | Q(sub_title__icontains=word) | Q(titleheading__icontains=word)

        return biblio.filter(query).distinct().order_by('publishedYear').reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queries = self.request.GET['search']
        context['query'] = queries
        biblio = self.biblio
        query = Q()

        for word in queries.split():
            query |= Q(responsibility__icontains=word) | Q(authorheading__icontains=word)

        context['responsibility'] = biblio.filter(query).distinct()

        return context
