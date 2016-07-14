"""mohsinulhaq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Github.as_view(), name='index'),
    url(r'^autocomplete/$', views.Autocomplete.as_view(), name='autocomplete'),
    url(r'^radio/$', views.Radio.as_view(), name='radio'),
    url(r'^regex/$', views.Regex.as_view(), name='regex'),
    url(r'^facebook/$', views.Facebook.as_view(), name='facebook'),
    url(r'^pagination/$', views.Pagination.as_view(), name='pagination'),
    url(r'^test/$', views.Test.as_view(), name='test')
]
