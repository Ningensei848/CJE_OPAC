from django.db.models import Q
from django.views.generic import ListView

from opac.models.bibliography import BIBLIO
from opac.mylib.pagination import paginate_queryset


class ResultListView(ListView):
    template_name = 'opac/result_list.html'
    model = BIBLIO
    paginate_by = 20  # if pagination is desired
    biblio = BIBLIO.objects.all()

    def get_queryset(self):
        """
        #mainpage にわたすためのクエリセット
        """
        queries = self.request.GET['search']
        biblio = self.biblio
        query = Q()

        for word in queries.split():
            query |= Q(title__icontains=word) | Q(sub_title__icontains=word) | Q(titleheading__icontains=word)

        return biblio.filter(query).distinct().order_by('publishedYear').reverse()

    def get_context_data(self, **kwargs):
        """
        #mainpage 以外に渡すためのクエリセット
        """
        context = super().get_context_data(**kwargs)
        queries = self.request.GET['search']
        context['query'] = queries
        biblio = self.biblio
        query = Q()

        for word in queries.split():
            query |= Q(responsibility__icontains=word) | Q(authorheading__icontains=word)

        page_obj_responsibility = paginate_queryset(
            self.request,
            biblio.filter(query).distinct(),
            self.paginate_by
        )
        context['responsibility'] = page_obj_responsibility.object_list
        context['page_obj_responsibility'] = page_obj_responsibility

        return context
