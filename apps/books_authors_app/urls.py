from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^processing$', views.processing),
    url(r'^authors$', views.authors_home),
    url(r'^authors/(?P<id>[0-9]+)$', views.display_authors),
    url(r'^add_them$', views.add_them),
    url(r'^books/(?P<id>[0-9]+)$', views.display_books),
    url(r'^$', views.books_home),
]