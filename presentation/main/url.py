from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^page_one/$', views.page_one, name='page_one'),
    url(r'^page_two/$', views.page_two, name='page_two'),
    url(r'^page_three/$', views.page_three, name='page_three'),
    url(r'^page_four/$', views.page_four, name='page_four'),
    url(r'^page_five/$', views.page_five, name='page_five'),
    url(r'^page_six/$', views.page_six, name='page_six'),
    url(r'^page_seven/$', views.page_seven, name='page_seven'),
    url(r'^end/$', views.end, name='end'),
    url(r'^java_source/$', views.java_source, name='java_source'),
    url(r'^c_source/$', views.c_source, name='c_source'),
    url(r'^python_source/$', views.python_source, name='python_source'),
    url(r'^zen/$', views.zen, name='zen'),
]
