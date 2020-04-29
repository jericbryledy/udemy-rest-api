from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^postgres$', views.postgres, name='postgres'),
    url(r'^redis$', views.redis, name='redis')
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
app_name = 'query'
