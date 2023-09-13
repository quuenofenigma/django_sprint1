from django.urls import path

from .views import StaticPageAbout, StaticPageRules

app_name = 'pages'

urlpatterns = [
    path('about/', StaticPageAbout.as_view(), name='about'),
    path('rules/', StaticPageRules.as_view(), name='rules'),
]
