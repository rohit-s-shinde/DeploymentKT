from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r"hello/", views.hello),
    url(r"bye/", views.bye),
]
urlpatterns = format_suffix_patterns(urlpatterns)