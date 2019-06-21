from django.views.generic import DetailView

from opac.models.bibliography import BIBLIO
from opac.mylib.isbn_tools import isbn10_to_13
from opac.mylib.isbn_tools import confirm_source_exist

import re

pattern = re.compile(r"\[\'(.*?)\'")


class BiblioDetailView(DetailView):
    model = BIBLIO  # Equal ==> "queryset = Metadata.objects.all()"
    template_name = 'opac/biblio_detail.html'
    slug_field = 'nbc'
    slug_url_kwarg = 'nbc'

    def get_context_data(self, **kwargs):
        """
        書影API(openBD)から画像を持ってくる
        """

        context = super().get_context_data(**kwargs)
        nbc = self.kwargs.get('nbc')

        page_url = 'https://cgi.u.tsukuba.ac.jp/~s1611502/django.cgi/opac/detail/' + nbc
        context['page_url'] = page_url

        biblio = self.model
        source = biblio.objects.get(nbc=nbc)
        isbn = source.isbn
        if isbn is None:
            return context

        if pattern.match(isbn):
            m_list = pattern.findall(isbn)
            isbn_13 = isbn10_to_13(m_list[0])
        else:
            # print('not match')
            isbn_13 = isbn10_to_13(isbn)

        # if img source exist...
        img_src = confirm_source_exist(isbn_13)
        if img_src:
            context['openbd_img'] = img_src

        return context
