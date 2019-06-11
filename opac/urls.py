"""opac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path

from opac.views.index import IndexView
from opac.views.result_list import ResultListView
from opac.views.biblio_detail import BiblioDetailView

app_name = 'opac'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('result/', ResultListView.as_view(), name='result'),
    path('detail/<slug:nbc>/', BiblioDetailView.as_view(), name='biblio_detail'),
]
