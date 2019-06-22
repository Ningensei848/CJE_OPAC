from django.db.models import Q
from django.views.generic import ListView

from opac.models.bibliography import BIBLIO
from opac.mylib.pagination import paginate_queryset

from opac.forms.search import SearchForm


class ResultListView(ListView):
    template_name = 'opac/result_list.html'
    model = BIBLIO
    paginate_by = 20  # if pagination is desired
    biblio = BIBLIO.objects.all()

    def get_context_data(self, **kwargs):
        """
        #mainpage 以外に渡すためのクエリセット
        """
        context = super().get_context_data(**kwargs)
        form = SearchForm(self.request.GET)
        if not form.is_valid():
            return context
        else:
            # 検証前のデータを取り出せますが、検証済みのデータを使うのがよい方法
            # queries = self.request.GET['keywords'].strip()
            queries = form.cleaned_data['keywords'].strip()
            context['query'] = queries
            biblio = self.biblio

            # Title
            query_title = Q()
            for word in queries.split():
                query_title |= Q(title__icontains=word) | Q(sub_title__icontains=word) | Q(titleheading__icontains=word)

            page_obj_title = paginate_queryset(
                self.request,
                biblio.filter(query_title).distinct().order_by('publishedYear').reverse(),
                self.paginate_by
            )
            context['result_title'] = page_obj_title.object_list
            context['page_obj_title'] = page_obj_title

            # responsibility
            query_responsibility = Q()
            for word in queries.split():
                query_responsibility |= Q(responsibility__icontains=word) | Q(authorheading__icontains=word)

            page_obj_responsibility = paginate_queryset(
                self.request,
                biblio.filter(query_responsibility).distinct().order_by('publishedYear').reverse(),
                self.paginate_by
            )
            context['result_responsibility'] = page_obj_responsibility.object_list
            context['page_obj_responsibility'] = page_obj_responsibility

            # publication
            query_publication = Q()
            for word in queries.split():
                query_publication |= Q(publishedArea__icontains=word) | Q(publisher__icontains=word)

            page_obj_publication = paginate_queryset(
                self.request,
                biblio.filter(query_publication).distinct().order_by('publishedYear').reverse(),
                self.paginate_by
            )
            context['result_publication'] = page_obj_publication.object_list
            context['page_obj_publication'] = page_obj_publication

            # series
            query_series = Q()
            for word in queries.split():
                query_series |= Q(series__icontains=word)

            page_obj_series = paginate_queryset(
                self.request,
                biblio.filter(query_series).distinct().order_by('publishedYear').reverse(),
                self.paginate_by
            )
            context['result_series'] = page_obj_series.object_list
            context['page_obj_series'] = page_obj_series

            # ANY search
            query_any = Q()
            for word in queries.split():
                query_any |= Q(nbc__icontains=word)            | Q(isbn__icontains=word)           | \
                             Q(title__icontains=word)          | Q(sub_title__icontains=word)      | \
                             Q(responsibility__icontains=word) | Q(ed__icontains=word)             | \
                             Q(publishedArea__icontains=word)  | Q(publisher__icontains=word)      | \
                             Q(publishedYear__icontains=word)  | Q(publishedMonth__icontains=word) | \
                             Q(page__icontains=word)           | Q(size__icontains=word)           | \
                             Q(series__icontains=word)         | Q(note__icontains=word)           | \
                             Q(titleheading__icontains=word)   | Q(authorheading__icontains=word)  | \
                             Q(holdingsrecord__icontains=word) | Q(holdingphys__icontains=word)    | \
                             Q(holdingloc__icontains=word)

            page_obj_any = paginate_queryset(
                self.request,
                biblio.filter(query_any).distinct().order_by('publishedYear').reverse(),
                self.paginate_by
            )
            context['result_any'] = page_obj_any.object_list
            context['page_obj_any'] = page_obj_any

        return context
